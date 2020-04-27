#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'kDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#

def kDifference(a, k):
    a.sort()
    count=0
    l = len(a)
    for i in range(l):
        sub=i+1
        while sub<l and a[sub]<=a[i]+2:
            if a[sub]==a[i]+2:
                count+=1
            sub+=1
    return count
#idea make use of sorting it (and sets of some sort?) for faster checking

if __name__ == '__main__':

    a_count = 100#int(input().strip())

    a = [random.randint(0,1000) for i in range (a_count)]# []
    """
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)
    """

    k = random.randint(1,9) #int(input().strip())

    result = kDifference(a, k)

    print(str(result) + '\n')
