#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the oddNumbers function below.
def oddNumbers(l, r):
    array = [i for i in range(l,r+1) if i%2!=0]
    return array

if __name__ == '__main__':
    x = ""

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    x='\n'.join(map(str, res))
    
    print(x)
