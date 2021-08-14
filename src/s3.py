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
import botostubs, boto3
from core.aws_config import AWSConfig
from fuzzysearch import find_near_matches

config = AWSConfig()
client = config.session.client('s3') # type: botostubs.S3

def list_buckets(search_filter):
    try:
        response = client.list_buckets()
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            for item in search_list(search_filter, 'Name', response['Buckets']):
                print(item['Name'])
    except botocore.exceptions.ClientError as error:
        raise error


def search_list(term, key, search_list):
    ''' Searches a list for a given key and value.
    '''
    if(not search_list or not key or not term):
        return search_list
    
    filtered = list()
    for item in search_list:
        if find_near_matches(term, item[key], max_l_dist=1):
            filtered.append(item)
    
    return filtered


if len(sys.argv) > 1:
    list_buckets(sys.argv[1])
else:
    list_buckets(None)

exit(0)