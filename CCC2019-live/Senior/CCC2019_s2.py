# CCC2019_s2.py
# Evan Kanter
# 2019-02-20

def isPrime(n):
    for j in range(2, int(n / 2) + 1):
        if n % j == 0 and (j != 1 and j != n):
            return False
    return True


T = int(input())
lines = [int(input()) for each in range(0, T)]

primes = []
for j in range(2, int(max(lines) * 1.75)):
    if isPrime(int(j)):
        primes.append(j)

nextLine = False
for each in lines:
    nextLine = False
    for i in primes:
        for k in primes:
            if (i + k) / 2 == each:
                print(str(i) + " " + str(k))
                nextLine = True
                break
        if nextLine:
            break
