#NEW VERSION - 2
# Coded By: Evan Kanter - University of Toronto Schools
# CCC 2017 - Problem J4: Favourite Times

D=int(input())

counter=0
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
	
	
myList=[1,5,5,4,4,3,3,2,2,1,0,1]

numberofHDays=D//(60*12)
for i in range (0,numberofHDays):
	answer+=31

numberofHours=(D%(60*12))//60
while counter	< numberofHours: #NOTE its not <= because we use it for a list
	answer+=myList[counter]
	counter+=1

# the following code calculates the number of times in the last hour
if numberofHours>0:
	extraHour=str(numberofHours+1)
	if int(extraHour)>9:
		h=int(extraHour[0])
		hH=int(extraHour[1])
	else:
		h=0
		hH=int(extraHour)
else:
	h=1
	hH=2
	
numberofmin=(D%(60*12))%60


m=0
mM=0
	
counter=0
while counter <=numberofmin:

	if h==0 and hH-m==m-mM or h-hH==hH-m==m-mM:
		answer+=1
		##time=str(h)+str(hH)+":"+str(m)+str(mM)
		##print("Logged an addition at" + time)
	mM+=1
	shift()
	counter+=1
	
print(answer)


	
