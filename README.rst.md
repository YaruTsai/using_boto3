Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allow Python developers to write software that makes use of services like Amazon S3 and Amazon EC2 or Ceph S3.

# Quick Start

## Install pip
```
$ apt-get install python3-pip
```
or 2.x version
```
$ apt-get install python-pip
```
### check pip version
```
$ pip --version
```
## Install boto3
```
$ pip install boto3
```

# How to connect to Ceph S3
```
import boto3

# Default connect
s3 = boto3.client('s3',
        aws_access_key_id = 'your_access_key_id',
        aws_secret_access_key = 'your_secret_access_key',
        endpoint_url = 'http://your_url:7480',
)
```