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
        bucket = aws_s3.Bucket(self, "BimboResultsV1")

        s3_resfile = aws_lambda.Function(self, 
                                         id="S3resFileV1",
                                         code=aws_lambda.Code.from_asset("./jarvis/compute"),
                                         handler="resultsHandler.lambda_handler",
                                         runtime=aws_lambda.Runtime.PYTHON_3_9)
        s3_resfile.add_to_role_policy(aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:PutObject", "s3:GetObject"],
            resources=["arn:aws:s3:::s3resultsstack-bimboresultsv17e612199-u9rm5tf6tgj5/*"]
            )
        )