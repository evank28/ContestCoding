#P2 - Youre Dead
NSL=input().split()
N=int(NSL[0])
S=int(NSL[1])
L=int(NSL[2])
T=[]
Tmod=[]
days=1
for i in range (N):
	T.append(int(input()))
for i in range (N):
	Tmod+=[T.pop(T.index(min(T)))]

lastvalue=Tmod[0]
counter=0
index=0

def newDay(id):
	global days
	global counter
	global lastvalue
	global day
	days+=1
	counter=1
	if (index+1)!=len(Tmod):
		lastvalue=Tmod[index+id]

	
for i in Tmod:
	counter+=1
	if S<=N:
		if counter>S:
			newDay(0)
	else:
		if counter>N:
			newDay(0)		
			
	if abs(i-lastvalue)>L:
		newDay(0)
		
	index+=1

print(days)