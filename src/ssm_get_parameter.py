#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title SSM Get parameter
# @raycast.mode fullOutput
# @raycast.packageName AWS

# Optional parameters:
# @raycast.icon images/aws-logo-light.png
# @raycast.argument1 { "type": "text", "placeholder": "parameter key", "optional": false}

# Documentation:
# @raycast.description SSM Get parameter
# @raycast.author Jerome Erasmus
# @raycast.authorURL https://github.com/JeromeErasmus

import sys
import botocore
import botostubs
import boto3
from collections import OrderedDict
from core.config import AWSConfig
from core.requests import AWSRequests
from core.functions import Functions, Fontcol

config = AWSConfig()
client = config.session.client('ssm')  # type: botostubs.SSM
table_headers = {'Name': 'Name', 'Value': 'Value'}
table_columns = {'Name', 'Value'}


def get_parameter(*args):
    response = AWSRequests.send_request(
        client.get_parameter,
        Name=args[0]
    )
    Functions.display([response['Parameter']], table_headers, table_columns)
    Functions.copyClipboard(response['Parameter']['Value'])
    

if len(sys.argv) > 1:
    get_parameter(sys.argv[1])
else:
    get_parameter(None)

exit(0)
