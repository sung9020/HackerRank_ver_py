#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#TODO
# Complete the freqQuery function below.
def freqQuery(queries):
    array = []
    stack = []
    result = ''
    for query in queries:
        if query[0] == 1:
            array.append(query[1])
            if query[1] in dict.keys():
                dict[query[1]] += 1
            else:
                dict.setdefault(query[1], 1)

            if dict[query[1]] > stack[-1]:
                stack.append(dict[query[1]])
        elif query[0] == 2:
            if query[1] in array:
                array.remove(query[1])
                if query[1] in dict.keys():
                    dict[query[1]] -= 1
        else:
            period = query[1] # period
            dict = Counter(array)
            if period in dict.values():
                result += '1'
            else:
                result += '0'
    return result

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print('\n'.join(map(str, ans)))

