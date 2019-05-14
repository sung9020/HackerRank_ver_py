#!/bin/python3

import math
import os
import random
import re
import sys
#TODO
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = sortString(a)
    b = sortString(b)
    a_index_list = set()
    b_index_list = set()

    for a_index, char in enumerate(a):
        b_index = b.find(char)
        if b_index > -1:
            a_index_list.add(a_index)
            b_index_list.add(b_index)
            b = b[:b_index] + '_' + b[b_index+1:]
    result = len(a) - len(a_index_list)
    result += len(b) - len(b_index_list)

    return result

def sortString(str):
    return ''.join(sorted(str))

if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)