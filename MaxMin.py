#!/bin/python3

import math
import os
import random
import re
import sys
# 순서대로 정렬됐을 때 i에서 k번째 수와 i에 위치한 수의 차이가 가장 작은 값을 구한다. 그럼 끝남
# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    min = arr[0 + k - 1] - arr[0]
    for i in range(0,len(arr)-k + 1):
        if min > arr[i+k-1] - arr[i]:
            min = arr[i+k-1] - arr[i]
    return min

if __name__ == '__main__':

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)