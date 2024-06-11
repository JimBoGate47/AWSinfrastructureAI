import json
import boto3

def lambda_handler(event, context):
    message = 'Hello Jimbo Bimbo!'
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message})
    }

def lambdaS3_handler(event, context):
    s3 = boto3.client('s3')
    # textract = boto3.client('textract')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    #file_content = response['Body'].read()

    message = 'Something was uploaded!'
    print("INFOi::")
    print({'name': key, 'body': response})
    print("INFOf::")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message,
                            "filename": key})
    }