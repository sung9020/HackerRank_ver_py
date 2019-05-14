#!/bin/python3

import math
import os
import random
import re
import sys
#TODO
# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    isUsed = [False]*len(s)

    for i in range(0,len(s) - 1):
        if s[i] == 'A':
            if s[i+1] != 'B':
                isUsed[i+1] = True
        else:
            if s[i+1] != 'A':
                isUsed[i+1] = True
    result = isUsed.count(True)
    return result
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)