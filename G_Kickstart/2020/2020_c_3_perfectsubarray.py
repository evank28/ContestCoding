# Google Kickstart 2020 Round C
# Code By Evan Kanter
# Solved 2020-05-17, live
import math

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        arr = list(map(int, input().split(" ")))
        count = 0
        # subs = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                sub_sum = sum(arr[i:j])
                if math.sqrt(sub_sum).is_integer():
                    count += 1
                    # subs.append(arr[i:j])
        print("Case #{}: {}".format(t,count))
