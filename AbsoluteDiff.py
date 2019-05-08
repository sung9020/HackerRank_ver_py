#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    i = 0
    j = 0
    arr.sort()
    min = abs(arr[1] - arr[0])

    while True:
        if min > abs(arr[i+1] - arr[i]):
            min = abs(arr[i+1]- arr[i])

        if i+1 == (len(arr)-1):
            break
        else:
            i += 1

    return min

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)

