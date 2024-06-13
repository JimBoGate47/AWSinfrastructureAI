#!/usr/bin/env python3
import aws_cdk as cdk
from jarvis.jarvis_stack import JarvisStack
from jarvis.s3bucket_stack import S3bucketStack
from jarvis.s3results_stack import S3ResultsStack

app = cdk.App()
jarvisStack = JarvisStack(app, "JarvisStack")
buckStack = S3bucketStack(app, "S3bucketStack")
buckResStack = S3ResultsStack(app, "S3ResultsStack")
jarvisStack.add_external_policy(buckResStack.build_external_policy(["s3:GetObject",
                                                                    "s3:ListBucket"]))
buckStack.add_external_policy(buckResStack.build_external_policy(["s3:PutObject", 
                                                                  "s3:GetObject",
                                                                  "s3:ListBucket"]))
app.synth()
