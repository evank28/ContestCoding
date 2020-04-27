#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    checked=[]
    pairs=0
    for sock in ar:
        if sock not in checked:
            pairs+=ar.count(sock)//2
            checked+=[sock]
    return pairs

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    print(str(result) + '\n')
