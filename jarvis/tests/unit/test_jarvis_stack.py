import aws_cdk as core
import aws_cdk.assertions as assertions

from jarvis.jarvis_stack import JarvisStack

# example tests. To run these tests, uncomment this file along with the example
# resource in jarvis/jarvis_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = JarvisStack(app, "jarvis")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
