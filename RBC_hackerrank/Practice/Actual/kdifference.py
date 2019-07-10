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
    diffs=list(map(lambda x:x-k,a))
    diffs2=list(map(lambda x:x+k,a))
    count=0
    for i in range(len(a)):
        count+=diffs[i+1:].count(a[i])+diffs2[i+1:].count(a[i])
    return count

if __name__ == '__main__':

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    k = int(input().strip())

    result = kDifference(a, k)

    print(str(result) + '\n')
