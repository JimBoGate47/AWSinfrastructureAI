#!/usr/bin/env python3
import os

import aws_cdk as cdk

from jarvis.jarvis_stack import JarvisStack
from jarvis.s3bucket_stack import S3bucketStack
# from jarvis.s3results_stack import S3ResultsStack

app = cdk.App()
JarvisStack(app, "JarvisStack")
S3bucketStack(app, "S3bucketStack")
# S3ResultsStack(app, "S3ResultsStack")
app.synth()
