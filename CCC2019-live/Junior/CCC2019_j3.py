#CCC2019_j3.py
#Evan Kanter
#2019-02-20
N = int(input())
lines = [str(input()) for each in range (0,N)]

import time
start_time = time.time()   

for line in lines:
    outLine, i, curCharCount = "", 1, 1
    while i<len(line):
        if line[i] == line[i-1]:
            curCharCount += 1
            if i == len(line)-1:
                outLine = outLine + str(curCharCount) + " " + line[i]
        else:
            outLine = outLine + str(curCharCount) + " " + line[i-1] + " "
            curCharCount = 1
            if i == len(line)-1:
                outLine = outLine + str(1) + " " + str(line[i])
        i+=1
    print(outLine)
end_time = time.time()
print(end_time-start_time)