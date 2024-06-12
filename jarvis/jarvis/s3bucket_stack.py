from aws_cdk import (
    Stack,
    aws_s3,
    aws_lambda,
    aws_iam
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
                                         handler="readDataHandler.lambda_handler",
                                         runtime=aws_lambda.Runtime.PYTHON_3_9)
        s3_newfile.add_to_role_policy(aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:GetObject"],
            resources=[bucket.arn_for_objects("*")]
            )
        )

        s3_newfile.add_to_role_policy(aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["textract:AnalyzeDocument", 
                     "textract:StartDocumentAnalysis",
                     "textract:GetDocumentAnalysis"],
            # resources=["arn:aws:textract:*:*:/adapters/*",
            #            "arn:aws:textract:*:*:document/*"]
            resources=["*"] # FIXME
            )
        )

        s3_newfile.add_to_role_policy(aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:PutObject"],   
            resources=["arn:aws:s3:::s3resultsstack-bimboresultsv17e612199-u9rm5tf6tgj5/*"]
            )
        )

        event_src = S3EventSourceV2(bucket=bucket,
                                        events=[aws_s3.EventType.OBJECT_CREATED_PUT])
        s3_newfile.add_event_source(event_src)