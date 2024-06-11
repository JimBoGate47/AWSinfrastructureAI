from aws_cdk import (
    Stack,
    aws_s3,
    aws_lambda
)
from aws_cdk.aws_lambda_event_sources import S3EventSourceV2
from constructs import Construct

class S3bucketStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = aws_s3.Bucket(self, "BimboBucketV1")
        s3_newfile = aws_lambda.Function(self, 
                                         id="S3newFileV1",
                                         code=aws_lambda.Code.from_asset("./jarvis/compute"),
                                         handler="helloHandler.lambdaS3_handler",
                                         runtime=aws_lambda.Runtime.PYTHON_3_9)
        
        event_src = S3EventSourceV2(bucket=bucket,
                                        events=[aws_s3.EventType.OBJECT_CREATED_PUT])
        s3_newfile.add_event_source(event_src)