# Coded By: Evan Kanter - University of Toronto Schools
# CCC 2017 Problem J3 : Exactly Electrical
a = input()
spaceDistance = a.index(" ")
startPos = [int(a[:spaceDistance]), int(a[spaceDistance + 1:])]

# Prints the Starting Coordinate -
# print ("("+str(startPos[0])+","+str(startPos[1])+")")

b = input()
spaceDistance = b.index(" ")
endPos = [int(b[:spaceDistance]), int(b[spaceDistance + 1:])]

t = int(input())  # charge

xDistance = abs(startPos[0] - endPos[0])
yDistance = abs(startPos[1] - endPos[1])
totalDistance = xDistance + yDistance
totalDiff = abs(totalDistance - t)
answer = "N"
# if totalDistance is greater than t then the answer is by default "N"

if totalDiff == 0:
    answer = "Y"
elif totalDiff > 0:
    if totalDiff == 1:
        answer = "N"
    if totalDiff % 2 == 0:
        answer = "Y"
    else:
        answer = "N"

print(answer)
