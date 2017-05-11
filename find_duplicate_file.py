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
            all_files.append(file)
    return all_files

def find_duplicate_file(abspath):
    """
    @path: Direct path
    """
    __all_files__ = dict(Counter(get_all_files(abspath)))
    for key in __all_files__:
        if __all_files__[key] > 1:
            file_abspaths = find_file_abspath(abspath, key)
            print('Duplicate times:\t'+ str(__all_files__[key]))
            print("Duplicate file name:\t" + key)
            print("Duplicate file path:")
            for file_abspath in file_abspaths:
                print("  " + file_abspath)
            print('\n')
            print("-" * 100)

def find_file_abspath(direct_path, direct_file):
    """find_file_abspath"""
    result = []
    for dirpath, _, allfiles in os.walk(direct_path):
        separator = "" if dirpath[len(dirpath) - 1] == "/" else "/"
        for file in allfiles:
            if file == direct_file:
                result.append(dirpath + separator + file)
    return result

# get path from command
__relpath__ = os.getcwd()
if len(sys.argv) > 1:
    __relpath__ = sys.argv[1]
__abspath__ = os.path.abspath(__relpath__)

find_duplicate_file(__abspath__)
