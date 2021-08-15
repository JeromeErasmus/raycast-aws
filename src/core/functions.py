"""Core AWS config Class
"""

# Copyright (C) 1999-2021 Jerome Erasmus
# Written by Jerome Erasmus


import boto3
from botocore.config import Config
from fuzzysearch import find_near_matches

__all__ = ['Functions', 'search_list']

class Functions:
  
  @staticmethod
  def search_list(term, key, search_list):
    ''' Searches a list for a given key and value.
    '''
    if(not search_list or not key or not term):
        return search_list

    filtered = list()
    for item in search_list:
        if find_near_matches(term, item[key], max_l_dist=1):
            filtered.append(item)

    return filtered


