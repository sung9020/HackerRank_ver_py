#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 0 # 인덱스를 찾는거 자체가 시간을 낭비 시킴 find, index 함부로 사용 금물
    while i < len(arr):
        if arr[i] != i + 1:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            count += 1
            i -= 1
        i += 1
    return count

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)