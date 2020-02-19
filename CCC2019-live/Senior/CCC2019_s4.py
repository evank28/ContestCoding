# CCC2019_s2.py
# Evan Kanter
# 2019-02-20
# FINISHED JUST AFTER DEADLINE!! :|

in1 = str(input()).split(" ")
N = int(in1[0])
K = int(in1[1])
scores = list(map(int, input().split(" ")))
sScores = sorted(scores)
is_max = [False] * len(scores)
if N % K == 0:
    days = int(N / K)
else:
    days = int(N / K + 1)

days_left = days
j_counter = len(sScores) - 1
while days_left > 0:
    for index in range(0, len(scores) - 1):
        if scores[index] == sScores[j_counter]:
            j_counter -= 1
            is_max[index] = True
            days_left -= 1

        if days_left < 1:
            break
# calculate number of days needed
max_score = 0

for index in range(0, len(scores) - 1):
    if is_max[index]:
        max_score += scores[index]

print(max_score)

"""
WRONG BECAUSE IT DOES NOT DO IT IN ORDER
scores=sorted(list(map(lambda x:int(x),input().split(" "))))


#splits the max values across each day
maxScore=0
iCounter=len(scores)-1
for day in range(0,days):
        maxScore+=scores[iCounter]
        iCounter-=1

print(maxScore)
"""
