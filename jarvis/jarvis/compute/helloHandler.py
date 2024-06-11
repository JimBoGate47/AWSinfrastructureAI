import json
import boto3

def lambda_handler(event, context):
    message = 'Hello Jimbo Bimbo!'
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message})
    }