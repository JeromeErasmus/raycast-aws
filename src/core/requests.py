"""Core AWS Class
"""

# Copyright (C) 1999-2021 Jerome Erasmus
# Written by Jerome Erasmus


import boto3, botocore

__all__ = ['AWSRequests', 'send_request']

class AWSRequests:

  @staticmethod
  def send_request(client_request):
    """Handles AWS Boto response
    """
    try:
        return client_request()
    except botocore.exceptions.ClientError as error:
        raise error
