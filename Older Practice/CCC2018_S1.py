#CCC2018_S1:Voronoi Villages -- practice on 2019-02-18
#By: Evan Kanter

N = int(input())
villages=sorted([int(input()) for i in range(N)])

#print(villages)


smallest = villages[N-2]

for  i in range(1,N-1,1):
    left = (villages[i]-villages[i-1])/2
    right = (villages[i+1]-villages[i])/2
    neighborhood = abs(left) + abs(right)
    if neighborhood < smallest:
        smallest = neighborhood

print(format(smallest,'.1f'))