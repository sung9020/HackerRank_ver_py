#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    result = 0
    jump = 0
    for index, value in enumerate(q):
        if value - index - 1 > 2:
            print("Too chaotic")
            return

        for i in range(max(value -2, 0), index):
            if q[i] > value:
                result += 1
    print(result)
    return;

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
