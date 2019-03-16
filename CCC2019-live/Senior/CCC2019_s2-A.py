#CCC2019_s2.py
#Evan Kanter
#2019-02-20
from math import sqrt

T = int(input())
lines = [int(input()) for each in range (0,T)]

max = 2*max(lines)

## THE FASTER ALTERNATIVE APPROACH TO THIS IS TO CREATE A BOOLEAN LIST TO DISTINGUISH PRIMES UP TO 2*max
isPrime = [True for i in range (0, max+1)]

for j in range (2,int(sqrt(max))):
    if isPrime[j]:
        for k in range (j, max+1,j):
            isPrime[k]=False

for each in lines:
    for i in range(0,max):
       if isPrime[i] and isPrime[each*2-i]:
           print(str(i)+" "+str(each*2-i))
           break