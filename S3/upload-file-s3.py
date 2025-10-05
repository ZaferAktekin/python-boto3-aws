# Upload file to s3

import boto3

s3 = boto3.client('s3')

# Specify a file to upload in s3

filename = 'test-boto3.txt' # File name to be uploaded
bucket_name = '' # The bucket name that the file will be uploaded


s3.upload_file(filename, bucket_name, modify_name)