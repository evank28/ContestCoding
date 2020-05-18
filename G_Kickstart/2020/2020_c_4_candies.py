# Google Kickstart 2020 Round C
# Code By Evan Kanter
# Solved 2020-05-17, live


def insert_before_a(base: str, a: str, to_insert: str) -> str:
    ind = base.find(a)
    return base[:ind] + to_insert + base[ind:]


def swap(base: str, i1: int, i2: int) -> str:
    """precondition: i1 > i2"""
    return base[:i2] + base[i1] + base[i2+1:i1] + base[i2] + base[i1+1:]


if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        R, C = list(map(int, input().split(" ")))
        rows = [input() for _ in range(R)]

        print("Case #{}: {}".format(t,out))
