#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'newPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def newPassword(a, b):
    """
    >>> newPassword('abc', 'def')
    'adbecf'
    >>> newPassword('cat', 'rabbit')
    'craatbbit'
    """
    if len(a) > len(b):
        return combine(a[:len(b)], b) + a[len(b):]
    elif len(a) < len(b):
        return combine(a, b[:len(a)]) + b[len(a):]
    else:
        return combine(a, b)

def combine(a, b):
    """
    >>> combine('abc', 'def')
    'adbecf'
    """
    assert len(a) == len(b)
    out = ""
    for i in range(len(a)):
        out += a[i]
        out += b[i]
    return out
