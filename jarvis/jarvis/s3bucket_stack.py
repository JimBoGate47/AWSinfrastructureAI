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
        self.__s3_newfile = aws_lambda.Function(self, 
                                         id="S3newFileV1",
                                         code=aws_lambda.Code.from_asset("./jarvis/functions"),
                                         handler="readDataHandler.lambda_handler",
                                         runtime=aws_lambda.Runtime.PYTHON_3_9)
        self.__s3_newfile.add_to_role_policy(aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:GetObject"],
            resources=[bucket.arn_for_objects("*")]
            )
        )

        self.__s3_newfile.add_to_role_policy(self.build_textract_policy())
        self.__s3_newfile.add_event_source(self.build_event(bucket))
        self.__s3_newfile.add_layers(self.build_layer())

    def add_external_policy(self, external_policy):
        self.__s3_newfile.add_to_role_policy(external_policy)
    
    def build_layer(self):
        return aws_lambda.LayerVersion(self, "AIlayer",
                                code=aws_lambda.AssetCode("./jarvis/layers/ailayer"),
                                compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_9])
    
    def build_event(self, bucket):
        return S3EventSourceV2(bucket=bucket,
                        events=[aws_s3.EventType.OBJECT_CREATED_PUT])
    
    def build_textract_policy(self):
        return aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["textract:AnalyzeDocument", 
                     "textract:StartDocumentAnalysis",
                     "textract:GetDocumentAnalysis"],
            # resources=["arn:aws:textract:*:*:/adapters/*",
            #            "arn:aws:textract:*:*:document/*"]
            resources=["*"] # FIXME
            )