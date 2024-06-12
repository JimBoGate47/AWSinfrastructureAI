import json
import boto3
import logging
from time import sleep
import os

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.INFO)
textract = boto3.client('textract') 

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    __lambda = boto3.client("lambda")
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    if os.environ['APIAPI']:
        print(os.environ['APIAPI'])

    if key.endswith(".tif") or key.endswith(".png"):
        logger.info(f"Reading new file: {key}")
        _key = key.split(".")[0] + ".txt"
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
    else:
        logger.error("Jodimos!")
        
    # print(file_content)
    # payload = {"bucket": bucket, "key": key, "content": file_content}
    # response = __lambda.invoke(FunctionName="blablabla_handler",
    #                 InvocationType="Event",
    #                 Payload=json.dumps(payload))
    
    response = s3.put_object(
            Bucket=os.environ['S3BIMBORES'],
            Key=_key,
            Body=extracted_text
        )
    message = 'Something was uploaded!'
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message,
                            "filename": key})
    }

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