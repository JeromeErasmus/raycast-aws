#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title RDS Create DB Cluster Snapshot
# @raycast.mode fullOutput
# @raycast.packageName AWS

# Optional parameters:
# @raycast.icon images/aws-logo-light.png
# @raycast.argument1 { "type": "text", "placeholder": "DB cluster identifier"}
# @raycast.argument2 { "type": "text", "placeholder": "Snapshot name"}

# Documentation:
# @raycast.description RDS Create DB Cluster Snapshot
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


def create_db_cluster_snapshot(*args):
  response = AWSRequests.send_request(
    client.create_db_cluster_snapshot,
    DBClusterIdentifier=args[0],
    DBClusterSnapshotIdentifier=args[1]
  )

  if response is None or response['DBClusterSnapshot'] is None:
      print("Error creating snapshot")
      return False
  
  print("snapshot created: ", response['DBClusterSnapshot']['DBClusterSnapshotIdentifier'])


if len(sys.argv) == 3:
    create_db_cluster_snapshot(sys.argv[1], sys.argv[2])

exit(0)
