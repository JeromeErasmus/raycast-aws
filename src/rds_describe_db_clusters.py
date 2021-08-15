#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title RDS Describe DB Clusters
# @raycast.mode fullOutput
# @raycast.packageName AWS

# Optional parameters:
# @raycast.icon images/aws-logo-light.png
# @raycast.argument1 { "type": "text", "placeholder": "Cluster name filter", "optional": true}

# Documentation:
# @raycast.description RDS Describe DB Clusters
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
client = config.session.client('rds')  # type: botostubs.RDS
table_headers = {
    'DBClusterIdentifier': 'DBClusterIdentifier',
    'Status': 'Status',
    'BackupRetentionPeriod': 'Retention',
    'Capacity': 'Capacity',
    'EngineMode': 'EngineMode'}
table_columns = {'DBClusterIdentifier', 'Status',
                 'BackupRetentionPeriod', 'EngineMode', 'Capacity'}


def describe_db_clusters(*args):
    
    response = AWSRequests.send_request(
        client.describe_db_clusters
    )

    items = Functions.search_list(args[0], 'DBClusterIdentifier', response['DBClusters'])
    Functions.display(items, table_headers, table_columns)


if len(sys.argv) > 1:
    describe_db_clusters(sys.argv[1])
else:
    describe_db_clusters(None)

exit(0)
