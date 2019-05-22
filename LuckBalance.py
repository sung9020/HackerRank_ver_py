#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=lambda luck:luck[0])
    result = 0
    k_count = 0
    for i in contests:
        if i[1] == 1:
            k_count += 1

    if k_count == k:
        for j in contests:
            result += j[0]
    else:#  k_count > k
        rest = k_count - k
        for j in contests:
            if rest > 0 and j[1] == 1:
                result -= j[0]
                rest -= 1
            else:
                result += j[0]
    return result

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)