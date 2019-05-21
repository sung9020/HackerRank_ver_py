#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    dict = Counter(s)
    dict_value = {}
    for v in dict.values():
        if v not in dict_value:
            dict_value[v] = 1
        else:
            value = dict_value.get(v)
            dict_value[v] = value + 1

    if len(dict_value.keys()) < 3:
        if len(dict_value.keys()) == 2:
            keys = list(dict_value.keys())
            key = 0
            value = 0
            if dict_value[keys[0]] > dict_value[keys[1]]:
                key = keys[1]
                value = dict_value[keys[1]]
                if value == 1 and (key == 1 or abs(keys[0] - keys[1]) == 1):
                    return "YES"
                else:
                    return "NO"
            else:
                key = keys[0]
                value = dict_value[keys[0]]
                if value == 1 and (key == 1 or abs(keys[0] - keys[1]) == 1):
                    return "YES"
                else:
                    return "NO"
        else:
            return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result)