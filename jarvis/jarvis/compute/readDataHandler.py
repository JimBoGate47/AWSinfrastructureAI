import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    __lambda = boto3.client("lambda")
    # textract = boto3.client('textract')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read()
    print("READING:" + key)
    print(file_content)
    # payload = {"bucket": bucket, "key": key, "content": file_content}
    # response = __lambda.invoke(FunctionName="S3ResultsStack-S3resFileV1054A5FE4-Alhc3Vu89ekq",
    #                 InvocationType="Event",
    #                 Payload=json.dumps(payload))
    
    response = s3.put_object(
            Bucket="s3resultsstack-bimboresultsv17e612199-u9rm5tf6tgj5",
            Key=key,
            Body=file_content+"ADIOS MUNDO\n".encode('utf-8')
        )
    message = 'Something was uploaded!'
    print("INFOi::")
    print("text modified")
    print(response)
    print("INFOf::")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message,
                            "filename": key})
    }