#WTS n^4 + 165n^3 \in O( n^4 - n)
# Prove negation, that \forall n_0, c in R+, exists n such that n>= n0 and
# n^4 + 165n^3 > n^4 - n

# Simplify -- checking that n in O(n^2) -- TRUE
# Simplify -- checking that n^2 in O(n) -- FALSE
from progress.bar import IncrementalBar

LIM  =  2 ** 10
def approx_positive_rationals():
    y = 0.001
    while y < LIM:
        yield y
        y += 0.001

def approx_naturals():
    y = 0
    while y <LIM:
        yield y
        y += 1

SUF = "'%(percent).5f%% - %(eta)ds'"
def check_big_oh():
    with IncrementalBar('Processing', max=(10**6)*(LIM**3), suffix=SUF) as bar:
        for n_0 in approx_positive_rationals():
            for c in approx_positive_rationals():
                found_n = False
                for n in approx_naturals():
                    bar.next()
                    if n >= n_0 and n <= c * n**2:
                        found_n = True
                        break
                if not found_n:
                    return f"No n value for n_0={n_0}, c={n_0}."

    return "The statement is true!"


if __name__ == "__main__":
    # print(check_big_oh())
    with IncrementalBar('Processing', max=LIM*1000,  suffix='%(percent).2f%% - %(eta)ds') as bar:
        for i in approx_positive_rationals():
            bar.next()

