# Google Kickstart 2020 Round E
# Code By Evan Kanter
# Solved 2020-08-23, live

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        N, A, B, C = map(int, input().split(" "))
        if A + B - C == N:
            # possible
            ls = [1 for i in range(1, A - C + 1)]
            rs = [1 for i in range(1, B - C + 1)]
            mid = [2 for i in range(C)]
            answer = ' '.join(ls) + ' ' + ' '.join(mid)  + ' '.join(rs)
        else:
            answer = 'IMPOSSIBLE'


        print("Case #{}: {}".format(t,answer))

 # if A + B + C <= N <=  A + B + C + 2:
        #     # possible
        # ls = [1 * i for i in range(1, A + 1)]
        # rs = [1 * i for i in range(1, A + 1)]
        #     if ls[-1] == rs[-1]:
        #         # then we consider the middle
        #     #otherwise, we know that 1 of them can be visible to both sides
        #     else:
        #         if C == N - A - B - 1:
        #             # then they are all equal height to the max of ls[-1] and rs[-1]
        #         else:
        #
        # else:
        #     answer = 'IMPOSSIBLE'
