#!/usr/bin/python

import boto3

# Default connect
s3 = boto3.client('s3',
        aws_access_key_id = 'your_access_key_id',
        aws_secret_access_key = 'your_secret_access_key',
        endpoint_url = 'http://your_url:7480',
)

bucket_name = 'bucket_name'

# Show object list
s3_list = s3.list_objects(Bucket=bucket_name)
print(s3_list)