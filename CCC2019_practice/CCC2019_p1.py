#j1
N = int(input())
ways =[]

for i in range (0,6):
    for j in range (0,6):
        if i+j==N and i>=j:
             ways.append((i,j))

print(len(ways))