# Google Kickstart 2020 Round B
# Code By Evan Kanter
# Solved 2020-04-18, live

t = int(input())
for t in range(1,t+1):
    N, D = [int(x) for x in input().split(" ")]
    line = [int(x) for x in input().split(" ")]
    cur_day = D

    for bus in line[::-1]:
        if cur_day % bus != 0:
            cur_day -= cur_day % bus
        # while cur_day % bus != 0 and cur_day >= 1:
        #     cur_day -= 1
    start_day = cur_day

    # start_day = 1
    # for d in range(1,D+1):
    #     cur_day = d
    #     for bus in line:
    #         while cur_day % bus != 0 and cur_day <= D:
    #             cur_day += 1
    #     if cur_day <= D:
    #         start_day = max(start_day, d)
    print("Case #{}: {}".format(t,start_day))
