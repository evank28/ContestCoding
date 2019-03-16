#s1
N = int(input())
swifts = list(map(lambda x:int(x),input().split(" ")))
sema = list(map(lambda x:int(x),input().split(" ")))

"""
K = 0
Kequal = 0
while K<=N:
        if sum(swifts[0:K]) == sum(sema[0:K]):
                Kequal=K
        K+=1

print(Kequal)
"""

Sswifts = sum(swifts)
Ssema = sum(sema)

""
K =N-1
while K>=0:
        Sswifts -= swifts[K]
        Ssema -= sema[K]
        if (Sswifts) == (Ssema):
                print(K+1)
                break
        K-=1
