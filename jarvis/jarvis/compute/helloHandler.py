import json

def lambda_handler(event, context):
    message = 'Hello Jimbo Bimbo!'
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message})
    }

def lambdaS3_handler(event, context):
    message = 'Something was uploaded!'
    print("INFOi::")
    print(event)
    print("INFOf::")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message})
    }