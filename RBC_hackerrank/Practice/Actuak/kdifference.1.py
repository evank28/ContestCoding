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
    sor = a.sort()
    count=0
    for i in range(len(sor)):
        sub=i+1
        while sor[sub]<=sor[i]+2:
            if sor[sub]==sor[i]+2:
                count+=1
            sub+=1
    return count
#idea make use of sorting it (and sets of some sort?) for faster checking
if __name__ == '__main__':

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    k = int(input().strip())

    result = kDifference(a, k)

    print(str(result) + '\n')
