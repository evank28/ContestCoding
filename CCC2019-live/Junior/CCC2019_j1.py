# CCC2019_j1.py
# Evan Kanter
# 2019-02-20
a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

scoreA = a1 + 2 * a2 + 3 * a3
scoreB = b1 + 2 * b2 + 3 * b3

if scoreA > scoreB:
    print("A")
elif scoreA == scoreB:
    print("T")
else:
    print("B")
