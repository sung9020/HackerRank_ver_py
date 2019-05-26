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
    stack = []
    rect = 0
    for i in range(len(h)):
        if i == 0:
            stack.append(i)
        elif h[stack[-1]] <= h[i]:
            stack.append(i)
        else:
            temp = stack.pop()
            if stack:
                rect = max(rect, h[temp] * (i - stack[-1] - 1)) # right-1 - stack.top
                stack.append(i)

    while stack:
        temp = stack.pop()
        if stack:
            rect = max(rect, h[temp] * (len(h) - stack[-1] - 1))
        else:
            rect = max(rect, h[temp] * (len(h) - 1))
    return rect

if __name__ == '__main__':
    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)
