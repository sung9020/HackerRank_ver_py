#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    ana_list = []
    ana_dict = {}
    bool_list = [True for i in range(len(s))]
    for i in range(1, len(s)):
        n_gram = list(zip(*[s[j:] for j in range(i)]))
        ana_list.extend([''.join(p) for p in n_gram])

    for key in ana_list:
        sort_key = sortString(key)
        if sort_key not in ana_dict:
            ana_dict.setdefault(sort_key, 1)
        else:
            ana_dict[sort_key] = ana_dict[sort_key]+1

    result = 0
    for value in ana_dict.values():
        if value > 1:
            result += combination(value, 2)

    return result

def combination(n, r):
    if n == r or r == 0:
        return 1
    else:
        return combination(n-1, r-1) + combination(n-1,r)

def sortString(str):
    return ''.join(sorted(str))

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)