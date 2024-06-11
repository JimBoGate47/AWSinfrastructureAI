import json

def lambda_handler(event, context):
    message = 'Hello from Lambda!'
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message})
    }