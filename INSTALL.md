# AWSinfrastructureAI

## Basic requirements:
- aws cli
- pip
- npm
- IAM Configured

# Install dependencies:
- npm i

## Into layers/ailayer folder:
- pip install -t python -r requirements.txt

## Into jarvis folder:
- pip install -r requirements.txt

# Deploy
- cdk deploy --all

# Environment variables
## On Stacks JarvisStack and S3bucketStack lambdas
- S3BIMBORES secondary_s3bucket_name