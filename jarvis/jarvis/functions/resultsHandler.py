import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.put_object(
            Bucket="s3resultsstack-bimboresultsv17e612199-u9rm5tf6tgj5",
            Key="prueba.txt",
            Body="ADIOS MUNDO\n".encode('utf-8')
        )
    print("INFOi::")
    print(response)
    print("INFOf::")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "done"})
    }