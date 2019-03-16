# Coded By: Evan Kanter - University of Toronto Schools
# CCC 2017 - Problem J4: Favourite Times

D=int(input())
h=1
hH=2
m=0
mM=0
counter=1
answer=0

def shift():
	global m
	global mM
	global h
	global hH
	time=str(h)+str(hH)+":"+str(m)+str(mM)
	
	while mM>9:
		m+=1
		mM-=10
		
	while m>5:
		hH+=1
		m-=6
	
	while int(str(h)+str(hH))>12:
		h=0
		hH=1
	
	time=str(h)+str(hH)+":"+str(m)+str(mM)
	
while counter <=D+1:

	if h==0 and hH-m==m-mM or h-hH==hH-m==m-mM:
		answer+=1
		#time=str(h)+str(hH)+":"+str(m)+str(mM)
		#print("Logged an addition at" + time)
	mM+=1
	shift()
	counter+=1
	
print(answer)
	
