#by Evan Kanter - UTS

h = int(input())
M = int(input())
value = False
t=1

while t<=M:
    A=-6*t**4 + h*t**3 + 2*t**2 + t
    if A <= 0:
        value = True
        break
    t+=1
    
if value:
    print("The balloon first touches ground at hour:")
    print(t)
else:
    print("The balloon does not touch ground in the given time.")
