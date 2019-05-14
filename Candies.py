#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    dp= []

    count = 0
    dp.append(1);

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dp.append(dp[-1] + 1)
        else:
            dp.append(1)

    for j in range (n - 1, 0, -1):
        if arr[j] < arr[j-1] and dp[j] >= dp[j - 1]:
            dp[j - 1] =  dp[j] + 1


    return sum(dp)

if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)
