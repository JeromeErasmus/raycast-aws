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
import pyperclip3
from core.config import AWSConfig
from core.requests import AWSRequests
from core.functions import Functions, Fontcol

config = AWSConfig()
client = config.session.client('ssm')  # type: botostubs.SSM

def describe_parameters(*args):
  response = AWSRequests.send_request(
    client.get_parameter,
    Name=args[0]
  )

  if response is None or response['Parameter'] is None:
    print('None found')
    return False

  pyperclip3.copy(response['Parameter']['Value'])

  print(Fontcol.WHITE, 'Name: ', response['Parameter']['Name'])
  print(Fontcol.YELLOW, 'Value: ', response['Parameter']['Value'])
  print(Fontcol.GREEN, 'Copied to clipboard')


if len(sys.argv) > 1:
    describe_parameters(sys.argv[1])
else:
    describe_parameters(None)

exit(0)
