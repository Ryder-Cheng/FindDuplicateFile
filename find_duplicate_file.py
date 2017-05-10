#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
find duplicate file
"""

import os
from collections import Counter
import sys

def get_all_files(abspath):
    """
    @abspath: get all files from path of 'abspath'
    @return: get list of all files
    """
    all_files = []
    for _, _, files in os.walk(abspath):
        for file in files:
            if file.find(".DS_Store") == -1:
                # print(file)
                all_files.append(file)
            else:
                continue
    return all_files

def find_duplicate_file(abspath):
    """
    @path: Direct path
    """
    __all_files__ = dict(Counter(get_all_files(abspath)))
    for key in __all_files__:
        if __all_files__[key] > 1:
            print('Duplicate ' + str(__all_files__[key] - 1) + ' times' + ":\t" + key)
            # print(key + ":\t" + str(__all_files__[key]))

# get path from command
__relpath__ = os.getcwd()
if len(sys.argv) > 1:
    __relpath__ = sys.argv[1]
__abspath__ = os.path.abspath(__relpath__)

find_duplicate_file(__abspath__)
