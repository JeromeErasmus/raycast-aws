#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Usage: get_sqs_messages.py <QUEUE_URL>
       get_sqs_messages.py -h | --help
"""

import json

import boto3
import docopt

def get_messages_from_queue(queue_url):
    sqs_client = boto3.client('sqs')

    messages = []
    
    while True:
        resp = sqs_client.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=10
        )

        try:
            messages.extend(resp['Messages'])
        except KeyError:
            break

        entries = [
            {'Id': msg['MessageId'], 'ReceiptHandle': msg['ReceiptHandle']}
            for msg in resp['Messages']
        ]
        print(entries)
    return messages

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    queue_url = args['<QUEUE_URL>']

    for message in get_messages_from_queue(queue_url):
        print(json.dumps(message))