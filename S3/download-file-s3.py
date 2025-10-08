# Download file from s3

import boto3

s3 = boto3.client('s3')

filename = 'test-boto3.txt' # File name to be downloaded
bucket_name = 'test-bucket-zafer' # The bucket name that the file will be downloaded