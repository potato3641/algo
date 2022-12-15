import sys
sys.setrecursionlimit(10**6)
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
def fact(n):
    if n in memo:
        return memo[n]
    else:
        flaga = False
        flagb = False
        if n-1 in memo:
            flaga = True
            nmo = memo[n-1]
        else:
            nmo = fact(n-1)
        if n-2 in memo:
            flagb = True
            nmt = memo[n-2]
        else:
            nmt = fact(n-2)
        if flaga and flagb and n-3 in memo:
            del memo[n-3]
        memo[n] = (n-1)*(nmo+nmt)%1000000000
        return memo[n]
# 선물 n-1 
memo = dict()
memo[5] = 44
memo[4] = 9
memo[3] = 2
memo[2] = 1
memo[1] = 0
memo[21] = 50944540
print(fact(N))
