# Google Kickstart 2020 Round E
# Code By Evan Kanter
# Started 2020-08-23, live
# Then, I got tired. Completed 2020-08-23, practice mode.


"""
This problem simplifies to a few cases.
Case 1: A + B - C > N. This translates to having more unique buildings visible than exist.
        This is impossible.
Case 2: A + B - C <= N

    Case 2.1: N = 1.
              This is the trivial case, where (since the first condition
    Case 2.2: N > 1. (Note: N cannot be less than 1)

        Case 2.2.1: C > 1.
                    This indicates there is more than one building that is commonly visible.
                    There may also be some buildings which are hidden.
                    In this case, just hide the hidden buildings between the common ones,
                    which can all be in the center.
        Case 2.2.2: C = 1. (Note: C cannot be less than 1)

                    Case 2.2.2.1: A = 1 and B = 1, and A + B - C  = 1 + 1 - 1 = 1 != N.
                                        This translates to having buildings that are not
                                        visible by either person, but no buildings to hide these
                                        invisible buildings between. This is impossible.
                    Case 2.2.2.1: A = 1 OR B = 1 OR A + B - C  = 1 + 1 - 1 = 1 = N.
                                        This means there is a single building visible by both
                                        people, and A-1 buildings visible
                                        to the left of the middle and B-1 buildings visible
                                        to the right of the middle. There are also H = N - A - B + 1
                                        hidden buildings. To make sure these are hidden, we choose
                                        either the left side or the right side based on whether
                                        there is at least one building there that these H buildings
                                        can be hidden behind. We then ensure these H buildings are
                                        shorter than the buildings that are hiding them, and then
                                        we are done.


"""

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        N, A, B, C = map(int, input().split(" "))
        if A + B - C > N:
            answer = 'IMPOSSIBLE'
        elif N == 1:
            answer = "1"
        elif C > 1:
            ls = "1 " * (A - C)
            rs = " 1" * (B - C)
            # hide those not visible in the middle
            mid = ("2 " * (C - 1)) + "1 " * (N - A - B + C) + "2"
            answer = ls + mid + rs

        # we know C = 1:
        elif A + B - C == N:
            # no buildings to hide
            ls = "1 " * (A - C)
            rs = " 1" * (B - C)
            # middle but nothing hidden
            mid = ("2 " * C)[:-1]
            answer = ls + mid + rs

        elif A > 1 or B > 1:
            ls = "2 " * (A - 1)
            rs = " 2" * (B - 1)
            mid = ("3 " * C)[:-1]
            if A > 1:
                ls += "1 " * (N - A - B + C)
            else:
                rs = " 1" * (N - A - B + C) + rs
            answer = ls + mid + rs

        else:
            # Then, A = 1 and B =1 and N=1 and C=1
            answer = 'IMPOSSIBLE'

        print("Case #{}: {}".format(t,answer))
