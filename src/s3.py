#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title S3 List Buckets
# @raycast.mode fullOutput
# @raycast.packageName AWS

# Optional parameters:
# @raycast.icon 🐓
# @raycast.argument1 { "type": "text", "placeholder": "bucket name filter", "optional": true}

# Documentation:
# @raycast.description List S3 Buckets
# @raycast.author Jerome Erasmus
# @raycast.authorURL https://github.com/JeromeErasmus

import botocore
import botostubs, boto3
from core.aws_config import AWSConfig

config = AWSConfig()
client = config.session.client('s3') # type: botostubs.S3

def list_buckets():
    try:
        response = client.list_buckets()
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            for item in response['Buckets']:
                print(item['Name'])
    except botocore.exceptions.ClientError as error:
        raise error

list_buckets()
