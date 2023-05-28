N, M = map(int,input().split())
A, B, C = N, N-M, M
mem = dict()
mem[0] = 1
mem[1] = 1
def dfs(n):
    if n not in mem:
        mem[n] = dfs(n-1)*n
    return mem[n]
print(dfs(A)//dfs(B)//dfs(C))
