# Google Kickstart 2020 Round C
# Code By Evan Kanter
# Solved 2020-05-17, live

T = int(input())
for t in range(1,T+1):
    N, K = list(map(int, input().split(" ")))
    # line = [int(x) for x in input().split(" ")]
    line = list(map(int, input().split(" ")))
    count = 0
    start = 0
    active = False
    # last = N-1
    for i, c in enumerate(line):
        if not active:
            if c == K:
                start = i
                active = True
        else:
            if c == K - (i-start) and i - start < K:
                continue
            else:
                if i - start >= K:
                    count += 1
                if c == K:
                    start = i
                else:
                    active = False
    if active and line[-1] == 1:
        count += 1
    print("Case #{}: {}".format(t,count))
