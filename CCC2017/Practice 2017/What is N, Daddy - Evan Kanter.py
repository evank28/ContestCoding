#coded by Evan Kanter, University of Toronto Schools
"""
n=int(input())
counter=int(0)

if n<6:
    counter+=1 #for n value
counter=counter+ n//2  #since 1&5 = 5&1 we divide by two but stay as an integer
    
print (counter)
"""

"""
for n in range (1,11):
 
    print ("Possibilities for INPUT:", n)
    if n<6:
        print (n)
    for j in range (1,n//2+1):
        print (n-j, "and", j)
"""

n=int(input())
counter=int(0)

if n<6:
    counter+=1 #for n value
for j in range (1,n//2+1):
    counter+=1
print(counter)

