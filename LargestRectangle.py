#!/bin/python3

import math
import os
import random
import re
import sys
#TODO
# Complete the largestRectangle function below.
def largestRectangle(h):
    k = 1
    min_list = []

    while k <= len(h):
        n_gram = tuple(zip(*[h[j:] for j in range(k)]))
        min_list.extend(set([min(value) * k for value in n_gram]))
        k += 1

    return max(min_list)

if __name__ == '__main__':
    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)
