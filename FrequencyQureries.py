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
    freq = Counter()
    cnt = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            cnt[ freq[value] ] -= 1
            freq[value] += 1
            cnt[ freq[value] ] += 1
        elif action == 2:
            cnt[ freq[value] ] -= 1
            if(freq[value] > 0):
                freq[value] -= 1
                cnt[ freq[value] ] += 1
        else:
            if cnt[value] > 0:
                result.append(1)
            else:
                result.append(0)

    return result

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print('\n'.join(map(str, ans)))

