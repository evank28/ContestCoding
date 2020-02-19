# CCC2019_j2.py
# Evan Kanter
# 2019-02-20
L = int(input())
lines = [input().split(" ") for each in range(0, L)]
for line in lines:
    print(int(line[0]) * str(line[1]))
