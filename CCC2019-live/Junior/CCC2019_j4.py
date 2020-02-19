# CCC2019_j4.py
# Evan Kanter
# 2019-02-20


flips = str(input())
grid = "1 2\n3 4"
V = flips.count("V")
H = flips.count("H")
newGrid = grid

v_needed = False
hNeeded = False

if V % 2 != 0:
    v_needed = True
if H % 2 != 0:
    hNeeded = True

if v_needed and hNeeded:
    newGrid = "4 3\n2 1"
elif hNeeded:
    newGrid = "3 4\n1 2"
elif v_needed:
    newGrid = "2 1\n4 3"

print(newGrid)
