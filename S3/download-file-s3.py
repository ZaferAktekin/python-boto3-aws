# Download file from s3

import boto3

s3 = boto3.client('s3')

filename = '' # File name to be downloaded
bucket_name = '' # The bucket name that the file will be downloaded

# Optional
modify_name = '' # Modifies the file name when downloading to the directory from s3

s3.download_file(bucket_name, filename, modify_name)