"""Core AWS config Class
"""

# Copyright (C) 1999-2021 Jerome Erasmus
# Written by Jerome Erasmus


import boto3
from botocore.config import Config
from collections import OrderedDict
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

    @staticmethod
    def pluck(items, keys):
        ''' Extracting specifix keys from dictionary

        Using dictionary comprehension + items()
        '''
        if not items or not keys:
            return False

        filtered = []
        for item in items:
            filtered.append(OrderedDict( {key: item[key] for key in item.keys() & keys}) )

        return filtered


class Fontcol:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'
