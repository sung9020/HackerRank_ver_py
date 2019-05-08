#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dict = {value: index for index, value in enumerate(cost)}
    for index, value in enumerate(cost):
        if value < money:
            beforeIndex = index
            afterIndex = dict.get(money - value)
            if afterIndex == None or beforeIndex == afterIndex:
                continue
            print(beforeIndex + 1 , afterIndex + 1, sep=" ")
            break;



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
