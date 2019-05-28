#!/bin/python3

import math
import os
import random
import re
import sys

cache = {0: 1, 1: 2, 2: 4}

# Complete the stepPerms function below.
def stepPerms(n):
    result = 0
    cut = [1, 1, 1]
    count = 0
    count += loopArray(n)
    return count

def loopArray(n):
    if n == 0: return 1
    if n < 0: return 0;

    if n - 1 in cache:
        return cache[n - 1]

    count = 0
    count += loopArray(n - 3) + loopArray(n - 2) + loopArray(n - 1)
    cache[n - 1] = count

    return count


if __name__ == '__main__':

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        print(res)
