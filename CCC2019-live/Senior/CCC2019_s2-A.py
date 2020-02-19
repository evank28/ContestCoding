# CCC2019_s2.py
# Evan Kanter
# 2019-02-20
from math import sqrt

T = int(input())
lines = [int(input()) for each in range(0, T)]

maximum = 2 * max(lines)

# THE FASTER ALTERNATIVE APPROACH TO THIS IS TO CREATE A BOOLEAN LIST TO
# DISTINGUISH PRIMES UP TO 2*maximum

isPrime = [True for i in range(0, maximum + 1)]

for j in range(2, int(sqrt(maximum))):
    if isPrime[j]:
        for k in range(j, maximum + 1, j):
            isPrime[k] = False

for each in lines:
    for i in range(0, maximum):
        if isPrime[i] and isPrime[each * 2 - i]:
            print(str(i) + " " + str(each * 2 - i))
            break
