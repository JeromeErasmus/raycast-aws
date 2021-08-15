"""Core AWS config Class
"""

# Copyright (C) 1999-2021 Jerome Erasmus
# Written by Jerome Erasmus


import boto3
from botocore.config import Config

__all__ = ['AWSConfig', 'get_client']


class AWSConfig:
    client = None
    session = None
    my_config = Config(
        region_name='ap-southeast-2',
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        }
    )

    def __init__(self):
        self.session = boto3.Session(profile_name='defaulr')

    def get_client(self, **kwargs):
        """Creates a AWS Client configuration
        """
        return self.client
