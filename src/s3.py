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

import sys
import botocore
import botostubs
import boto3
from core.config import AWSConfig
from core.requests import AWSRequests
from core.functions import Functions

config = AWSConfig()
client = config.session.client('s3')  # type: botostubs.S3


def list_buckets(search_filter):
    response = AWSRequests.send_request(client.list_buckets)

    if not response['Buckets']:
        return False

    for item in Functions.search_list(search_filter, 'Name', response['Buckets']):
        print(item['Name'])


if len(sys.argv) > 1:
    list_buckets(sys.argv[1])
else:
    list_buckets(None)

exit(0)
