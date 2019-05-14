#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = []

    dp.append(arr[0]) # 첫번째 값
    dp.append(max(arr[:2])) # 첫번째 값과 두번째 값 중에 최대
    for i in arr[2:]:
        dp.append(max([
            dp[-2] + i,
            i,
            dp[-1]
        ])
        )
    return dp[-1]

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)
