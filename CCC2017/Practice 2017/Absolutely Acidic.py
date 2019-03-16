#Solution to: Absolutely Acidic
#by Evan Kanter - UTS

N=int(input())
R=[]

Most=0
SecondMost=0

for i in range(0,N):
    R.append(int(input()))
    
def dif(First,Second):
    return abs(First-Second)

def MostToSecondMost():
    global Most
    global SecondMost
    if R.count(Most)== R.count(SecondMost):   #If Most is equal frequency to SecondMost
        if dif(Most,item)> dif(SecondMost,item): #then Is it of higher difference than Second Most with the new Most (AKA item)
            SecondMost=Most
    else: #If Most is more frequent than SecondMost(less frequent is impossible), then we transfer
        SecondMost=Most

                
#Lets find the most Frequent Term & the Second Most Frequent Term
for item in R:
    
        if R.count(item)> R.count(Most): #Is item highest Frequency
            #Should I Transfer Most To Second Most?
            MostToSecondMost()
            Most=item

            
        if R.count(item)== R.count(Most) and not item==Most: #Is item equal in Frequency to Most and not Most iteself?
            if dif(item,SecondMost)> dif(Most,SecondMost): #If Yes, then Is it of higher difference than the current value for Most? 
                MostToSecondMost()               
                Most=item
            
        if R.count(item)> R.count(SecondMost) and not item == Most: #Is it higher frequency than SecondMost and not Most
             SecondMost=item
             
        if R.count(item)== R.count(SecondMost)and not item == Most: #Is it equal frequency to SecondMost and not Most
            if dif(Most,item)> dif(Most,SecondMost):
                SecondMost=item


print (dif(Most,SecondMost))
