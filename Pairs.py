#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    count = 0
    arr_copy = set([i + k for i in arr])
    arr_set = set(arr)

    count = len(arr_copy.intersection(arr_set))
    return count


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)