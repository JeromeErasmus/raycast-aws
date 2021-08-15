#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title SSM Describe parameters
# @raycast.mode fullOutput
# @raycast.packageName AWS

# Optional parameters:
# @raycast.icon images/aws-logo-light.png
# @raycast.argument1 { "type": "text", "placeholder": "parameter name filter", "optional": true}

# Documentation:
# @raycast.description SSM Describe parameters
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
client = config.session.client('ssm')  # type: botostubs.SSM
table_headers = {'Name': 'Name', 'Type': 'Type'}
table_columns = {'Name', 'Type'}


def describe_parameters(*args):
    
    if args[0] is not None and len(args[0]) > 1:
        ParameterFilters = [
            {'Key': 'Name', 'Option': 'Contains', 'Values': [args[0]]}]
    else:
        ParameterFilters = []

    response = AWSRequests.send_request(
        client.describe_parameters,
        ParameterFilters=ParameterFilters,
        MaxResults=50
    )

    Functions.display(response['Parameters'], table_headers, table_columns)

if len(sys.argv) > 1:
    describe_parameters(sys.argv[1])
else:
    describe_parameters(None)

exit(0)
