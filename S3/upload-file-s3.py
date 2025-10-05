# Upload file to s3

import boto3

s3 = boto3.client('s3')

# Specify a file to upload in s3

filename = 'test-boto3.txt' # File name to be uploaded
bucket_name = '' # The bucket name that the file will be uploaded

# Optional
modify_name = 'modifiedboto3.txt' # Modifies the file name when uploading to s3

s3.upload_file(filename, bucket_name, modify_name)

print(f"{filename} has been uploaded to {bucket_name} Successfully")