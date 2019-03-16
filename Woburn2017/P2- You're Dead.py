#P2 - Youre Dead
NSL=input().split()
N=int(NSL[0])
S=int(NSL[1])
L=int(NSL[2])
T=[]
days=0
for i in range (N):
	T.append(int(input()))
while len(T)>0:
	counter=0
	i=0
	ex=T[0]
	if S<=N:
		while i<len(T):
			if counter<S:
				if abs(T[i]-ex)<=L:
					T.remove(T[i])
					counter+=1
					i-=1
			i+=1
		days+=1
	else:
		while i<len(T):
			if counter<N:
				if abs(T[i]-ex)<=L:
					T.remove(T[i])
					counter+=1
					i-=1
			i+=1
		days+=1
print(days)
