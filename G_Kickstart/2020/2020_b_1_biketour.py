# Google Kickstart 2020 Round B
# Code By Evan Kanter
# Solved 2020-04-18, live

t = int(input())
for t in range(1,t+1):
    N = int(input())
    line = [int(x) for x in input().split(" ")]
    count = 0
    if N > 2:
        for i in range(1,N-1):
            if line[i-1] < line[i] and line[i+1] < line[i]:
                count += 1
    print("Case #{}: {}".format(t,count))
