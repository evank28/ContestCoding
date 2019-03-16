#Carol's Cute Card
#Evan Kanter Feb 12 2018
def checkComp(signature):
    first=""
    second=""
    third=""
    tLen=len(signature)
    count=0
    while count<tLen:
        first=second
        second=third
        third=signature[count]
        if first=="C" and second=="C" and third=="C":
            return True
        count+=1
        
sig=str(input())

if checkComp(sig): 
    print("NO")
else:
    print("YES")