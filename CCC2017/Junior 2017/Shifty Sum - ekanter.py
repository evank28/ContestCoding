# Coded By: Evan Kanter - University of Toronto Schools
# CCC 2017 Problem #2 - Shifty Sum

#shifting = add 0 at end


N=input() #Starting number

Sum=int(N)
Shifter=int(N)

K = int(input()) #times to shift

counter=1
while counter <=K:

 Shifter*=10
 Sum+=Shifter
 counter+= 1
print (int(Sum))
