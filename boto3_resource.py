#!/usr/bin/python

import boto3

s3 = boto3.resource('s3',
        aws_access_key_id = 'your_access_key_id',
        aws_secret_access_key = 'your_secret_access_key',
        endpoint_url = 'http://your_url:7480',
)
print(s3)

bucket = s3.Bucket('bucket_name')
for obj in bucket.objects.all():
        bucket.download_file(obj.key,'/path/' + obj.key)