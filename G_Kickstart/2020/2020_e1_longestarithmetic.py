# Google Kickstart 2020 Round E
# Code By Evan Kanter
# Solved 2020-08-22, live

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        arr = list(map(int, input().split(" ")))
        longest = 0
        i, j = 0, 1
        difference = arr[j] - arr[0]
        while j < N:
            if arr[j] - arr[j-1] != difference:
                difference = arr[j] - arr[j - 1]
                i = j - 1
            longest = max(j - i + 1, longest)
            j += 1

        print("Case #{}: {}".format(t,longest))
