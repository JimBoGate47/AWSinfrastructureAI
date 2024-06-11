from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda
)
from constructs import Construct

class JarvisStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        helloWorld = aws_lambda.Function(self, 
                                         id="HelloWorldV1",
                                         code=aws_lambda.Code.from_asset("./jarvis/compute"),
                                         handler="helloHandler.lambda_handler",
                                         runtime=aws_lambda.Runtime.PYTHON_3_9)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "JarvisQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
