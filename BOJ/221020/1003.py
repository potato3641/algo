def fibo(n):
    if n==0:
        return 1, 0
    if n==1:
        return 0, 1
    if n not in memo:
        a1, a2 = fibo(n-1)
        b1, b2 = fibo(n-2)
        memo[n] = a1+b1, a2+b2
    return memo[n]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    memo = dict()
    print(*fibo(N))
