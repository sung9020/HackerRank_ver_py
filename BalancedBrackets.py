#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    open = ['(', '{', '[']
    close = [')', '}', ']']

    for char in s:
        if char in open:
            stack.append(char)
        else:
            if len(stack) > 0:
                open_e1 = stack.pop()
                open_e1_index = open.index(open_e1)
                if close[open_e1_index] != char:
                    return "NO"
            else:
                return "NO"

    if len(stack) > 0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)

