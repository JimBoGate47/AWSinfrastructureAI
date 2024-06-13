import json
import boto3
import os

def lambda_handler(event, context):
    message = 'Hello Jimbo Bimbo!'
    s3 = boto3.client("s3")
    data_files = run_text_extracted(s3, os.environ['S3BIMBORES'])
    _body = {"message": message,
             "data": data_files}
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': json.dumps(build_html(_body['message'], 
                                      _body['data'])),
    }

def run_text_extracted(client, bucket):
    def read_content (bucket, key):
        return client.get_object(Bucket=bucket,
                                     Key=key)['Body'].read().decode()
    response = client.list_objects_v2(Bucket=bucket)
    data_files = []
    for _obj in response['Contents']:
        if _obj['Key'].endswith(".data"):
            data_files.append({"filename": _obj['Key'].replace(".data", ""), 
                               "type": read_content(bucket, _obj['Key'])})
    return data_files

def build_html(title:str, rows:list)->str:
    table_rows = ""
    for _obj in rows:
        table_rows += f"<tr><td>{_obj['filename']}</td><td>{_obj['type']}</td></tr>"

    style = """
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .container {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>"""

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jarvis</title>
        {style}
    </head>
    <body>
        <div class='container'>
        <h1>{title}</h1>
        <table border="1">
            <tr><th>Filename</th><th>Type</th></tr>
            {table_rows}
        </table>
        </div>
    </body>
    </html>
    """
    return html_content.replace("\n", "")