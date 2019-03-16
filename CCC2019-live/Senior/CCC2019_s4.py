#CCC2019_s2.py
#Evan Kanter
#2019-02-20
#######FINISHED JUST!!! AFTER DEADLINE
in1 = str(input()).split(" ")
N = int(in1[0])
K = int(in1[1])
scores=list(map(int,input().split(" ")))
sScores = sorted(scores)
isMax = [False]*len(scores)
if N%K==0:
        days=int(N/K)
else:
        days=int(N/K+1)

daysLeft=days
jCounter=len(sScores)-1
while daysLeft>0:
        for index in range(0, len(scores)-1):
                if scores[index]==sScores[jCounter]:
                        jCounter-=1
                        isMax[index]=True
                        daysLeft-=1

                if daysLeft<1: break
#calculate number of days needed
maxScore=0

for index in range(0, len(scores)-1):
        if isMax[index]:
                maxScore+=scores[index]

print(maxScore)

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