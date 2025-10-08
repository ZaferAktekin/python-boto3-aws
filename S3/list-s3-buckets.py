# List S3 Buckets

import boto3

# Create an s3 client

s3 = boto3.client('s3')

# List all buckets

response = s3.list_buckets() 