# CCC2019_s2.py
# Evan Kanter
# 2019-02-20


def is_prime(n):
    for j in range(2, int(n / 2) + 1):
        if n % j == 0 and (j != 1 and j != n):
            return False
    return True


T = int(input())
lines = [int(input()) for each in range(0, T)]

maximum = max(lines)

primes = set()
for j in range(2, int(maximum * 1.75)):
    if is_prime(int(j)):
        primes.add(j)

nextLine = False
for each in lines:
    nextLine = False
    for i in primes:
        right = each * 2 - i
        if right in primes:
            print(str(i) + " " + str(right))
            nextLine = True
            break
        if nextLine:
            break
