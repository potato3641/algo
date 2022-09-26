def miis(): return map(int,input().split())
def dfs(n, cnt):
    global min_cnt
    if n%3==0:
        if min_cnt > cnt:
            dfs(n//3, cnt+1)
    if n%2==0:
        if min_cnt > cnt:
            dfs(n//2, cnt+1)
    if n == 1:
        if min_cnt > cnt:
            min_cnt = cnt
    if min_cnt > cnt:
        dfs(n-1, cnt+1)
min_cnt = 100000
N = int(input())
dfs(N, 0)
print(min_cnt)
