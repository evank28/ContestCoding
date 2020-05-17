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
        order = ""
        conditions = set()
        stable = True
        last = []
        shapes = set()
        for r, row in enumerate(reversed(rows)):
            if r > 0:
                for j, a in enumerate(row):
                    below = last[j]
                    if a != 'X':
                        if below == 'X':
                            stable = False
                            break
                        elif below != a:
                            condition = (below, a)
                            if condition not in conditions:
                                conditions.add(condition)
                        if a not in shapes:
                            shapes.add(a)
                if not stable:
                    break
            else:
                # top row
                for a in row:
                    if a != 'X':
                        shapes.add(a)
            last = row
        if stable:
            order = order.join(shapes)
            swaps = float('inf')
            while swaps:
                swaps = 0
                for before, after in conditions:
                    index_before = order.index(before)
                    index_after = order.index(after)
                    if index_before > index_after:
                        order = swap(order, index_before, index_after)
                        swaps += 1
            out = order
        else:
            out = -1
        print("Case #{}: {}".format(t,out))
