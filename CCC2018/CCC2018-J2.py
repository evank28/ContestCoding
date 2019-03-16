#CCC2018 J2
N=int(input())
yesterdayIn=str(input())
todayIn=str(input())

def splitPerDigit(word, length):
    count=0
    output=[]
    while count < length:
        output+=word[count]
        count+=1
    return output

#print(splitPerDigit(yesterdayIn, N))

yesterday=splitPerDigit(yesterdayIn, N)
today=splitPerDigit(todayIn, N)
#print("yesterday: ",yesterday,"/n", " today:", today)

count=0
numDoubOcc=0

while count < N:
    #print("yesterday: ",yesterday[count],"/n", " today:", today[count])
    if yesterday[count]=="C" and yesterday[count]==today[count]:
        numDoubOcc+=1
    count+=1

print(numDoubOcc)
