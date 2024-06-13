from aws_cdk import (
    Stack,
    aws_s3,
    aws_iam
)
from constructs import Construct

class S3ResultsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.__bucket = aws_s3.Bucket(self, "BimboResultsV1")

    def build_external_policy(self, actions:list):
        return aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=actions,
            resources=[self.__bucket.arn_for_objects("*"),
                       self.__bucket.bucket_arn]
        )