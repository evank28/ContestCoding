N=input()
OO=input().split()
O1=int(OO[0])
O2=int(OO[1])
choices=input().split()
happy=0
unhappy=0
choice1=int(choices.count("1"))
choice2=int(choices.count("2"))
if O1<choice1:
    happy=O1
    unhappy=choice1-O1
else:
    happy=choice1
    
if O2<choice2:
    happy+=O2
    unhappy+=choice2-O2
else:
    happy+=choice2
    
print(happy)

