from aws_cdk import (
    Stack,
    aws_lambda
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
from aws_cdk.aws_apigatewayv2 import HttpApi, HttpMethod
from constructs import Construct

class JarvisStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_world = aws_lambda.Function(self, 
                                         id="HelloWorldV2",
                                         code=aws_lambda.Code.from_asset("./jarvis/functions"),
                                         handler="helloHandler.lambda_handler",
                                         runtime=aws_lambda.Runtime.PYTHON_3_9)

        hello_world_integration = HttpLambdaIntegration(id="HelloWorldIntegration",handler=hello_world)
        http_api = HttpApi(self, "HelloWorldHttpApi")
        http_api.add_routes(path="/",
                            methods=[HttpMethod.GET],
                            integration=hello_world_integration)