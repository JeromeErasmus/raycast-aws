"""Core AWS Class
"""

# Copyright (C) 1999-2021 Jerome Erasmus
# Written by Jerome Erasmus


import boto3
import botocore

__all__ = ['AWSRequests', 'send_request']


class AWSRequests:

    @staticmethod
    def send_request(client_request, **kwargs):
        """Handles AWS Boto response
        """

        try:
            return client_request(**kwargs)
        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == 'LimitExceededException':
                print('API call limit exceeded; backing off and retrying...')
            else:
                print(error.response['Error']['Message'])
