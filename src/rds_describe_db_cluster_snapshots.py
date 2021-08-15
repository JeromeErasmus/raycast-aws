#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title RDS Describe DB Cluster Snapshots
# @raycast.mode fullOutput
# @raycast.packageName AWS

# Optional parameters:
# @raycast.icon images/aws-logo-light.png
# @raycast.argument1 { "type": "text", "placeholder": "Snapshot name filter", "optional": true}

# Documentation:
# @raycast.description RDS Describe DB Cluster Snapshots
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


def describe_db_clusters(search_filter):
    response = AWSRequests.send_request(client.describe_db_cluster_snapshots)

    if response is None or response['DBClusterSnapshots'] is None:
        print("None found")
        return False

    for item in Functions.search_list(search_filter, 'DBClusterSnapshotIdentifier', response['DBClusterSnapshots']):
        print(item['DBClusterSnapshotIdentifier'])


if len(sys.argv) > 1:
    describe_db_clusters(sys.argv[1])
else:
    describe_db_clusters(None)

exit(0)
