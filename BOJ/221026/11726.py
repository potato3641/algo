import sys
sys.setrecursionlimit(10**6)
def fibo(n):
    if n not in memo:
        memo[n] = fibo(n-1)+fibo(n-2)
    return memo[n]
N=int(input())
memo = dict()
memo[1] = 1
memo[2] = 2
print(fibo(N)%10007)
