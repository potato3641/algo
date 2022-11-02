def dfs(n):
    if n not in memo:
        adder = n-(n//2)*2
        if (n//2)+adder not in memo:
            memo[(n//2)+adder] = dfs((n//2)+adder)
        leftone = memo[(n//2)+adder]
        if n//2 not in memo:
            memo[n//2] = dfs(n//2)
        rightone = memo[n//2]
        memo[n] = (leftone*rightone)%C
    return memo[n]
A, B, C = map(int,input().split())
A %= C
memo = dict()
memo[0] = 1
memo[1] = A
print(dfs(B))
