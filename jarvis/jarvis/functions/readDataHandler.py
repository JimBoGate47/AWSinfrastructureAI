import json
import boto3
import logging
from time import sleep
import os
import re
from openai import OpenAI

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.INFO)
textract = boto3.client('textract') 

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    if key.endswith(".tif") or key.endswith(".png"):
        logger.info(f"Reading new file: {key}")
        _key = key.split(".")[0] + ".txt"
        extracted_text = run_text_extracted(s3, 
                                            os.environ['S3BIMBORES'], 
                                            _key)
        if extracted_text == '':
            extracted_text = run_textract(bucket, key)

        # text_results = analyze_text_ai(extracted_text)
        text_results = analyze_text_human(extracted_text)
    else:
        extracted_text = 'formato no admitido... valiste xD'
        text_results = "valiste xD"
        logger.error("Jodimos!")
    
    response = s3.put_object(
            Bucket=os.environ['S3BIMBORES'],
            Key=_key,
            Body=extracted_text
        )
    print(response)
    response = s3.put_object(
            Bucket=os.environ['S3BIMBORES'],
            Key=_key.replace(".txt", ".data"),
            Body=text_results
        )
    print(response)
    message = 'Something was uploaded!'
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message,
                            "filename": key})
    }

def run_text_extracted(client, bucket, key, prefix:str=''):
    response = client.list_objects_v2(Bucket=bucket,
                                      Prefix=prefix)
    for _obj in response['Contents']:
        if key == _obj['Key']:
            logger.info("File Loaded")
            return client.get_object(Bucket=bucket,
                                     Key=key)['Body'].read()
    return ''

def run_textract(bucket, key):
    textract_response = textract.start_document_analysis(
            DocumentLocation={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': key
                        }
            },
            FeatureTypes=['TABLES', 'FORMS']
        )
    job_id = textract_response['JobId']
    block_list = []
    get_analysis_result(job_id, next_token = None, block_list = block_list)

    extracted_text = ""
    for item in block_list:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + " "
    return extracted_text

def get_analysis_result(job_id, next_token, block_list):
    if(next_token == None):
        result = textract.get_document_analysis(JobId=job_id)
    else:
        result = textract.get_document_analysis(JobId=job_id, NextToken=next_token)
        
    blocks = result.get("Blocks")

    if(blocks != None):
        logger.info(f'Analysis blocks: {blocks}')
        block_list.extend(blocks)
        if(result.get("NextToken") != None):
            get_analysis_result(job_id, result["NextToken"], block_list )    
    else:
        logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Waiting to finish the analysis >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        logger.info(f'Analysis result: {result}')
        sleep(int(2))
        get_analysis_result(job_id, None, block_list)

def analyze_text_ai(cadena:str)->str:
    client = OpenAI()
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", 
                   "content": "Say this is a test"}],
    )
    logger.info("ChatGPT entrance")
    print(chat.choices[0].message.content)  # TODO Says give me money xD

def analyze_text_human(cadena:str)->str:
    if isinstance(cadena, bytes):
        cadena = cadena.decode()
    res = " ".join(re.findall(r'R.{1,3}\d{4,8}\b', cadena))
    if res == '':
        return 'NORMATIVA'.encode()
    return 'No-NORMATIVA'.encode()