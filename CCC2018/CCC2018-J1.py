#CCC2018 J1

d1=int(input())
d2=int(input())
d3=int(input())
d4=int(input())

def checkTelMark():
    if (d1==8 or d1==9) and (d4==8 or d4==9) and (d2==d3):
        return True
    return False
    
if checkTelMark():
    print("ignore")
else: print("answer")