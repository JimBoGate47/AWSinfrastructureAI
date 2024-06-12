from aws_cdk import (
    Stack,
    aws_s3,
    aws_lambda,
    aws_iam
)
from constructs import Construct

class S3ResultsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.__bucket = aws_s3.Bucket(self, "BimboResultsV1")

        # s3_resfile = aws_lambda.Function(self, 
        #                                  id="S3resFileV1",
        #                                  code=aws_lambda.Code.from_asset("./jarvis/functions"),
        #                                  handler="resultsHandler.lambda_handler",
        #                                  runtime=aws_lambda.Runtime.PYTHON_3_9)
        # s3_resfile.add_to_role_policy(aws_iam.PolicyStatement(
        #     effect=aws_iam.Effect.ALLOW,
        #     actions=["s3:PutObject", "s3:GetObject"],
        #     resources=[self.__bucket.bucket_arn]
        #     )
        # )
        
    def build_external_policy(self):
        return aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:PutObject"],
            resources=[self.__bucket.arn_for_objects("*")]
        )