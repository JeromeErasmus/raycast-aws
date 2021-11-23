#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Usage: sqs_redrive.py --src=<QUEUE_URL> --dst=<QUEUE_URL>
       sqs_redrive.py -h | --help
"""

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
    return messages


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    src_queue_url = args['--src']
    dst_queue_url = args['--dst']
    
    sqs_client = boto3.client('sqs')

    for message in get_messages_from_queue(src_queue_url):
         sqs_client.send_message(
             QueueUrl=dst_queue_url,
             Body=message['Body']
         )