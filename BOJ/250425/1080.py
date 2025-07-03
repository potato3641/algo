N, M = map(int,input().split())
A = [list(map(int, input())) for _ in range(N)]
try:
    B = [list(map(int, input())) for _ in range(N)]
except EOFError:
    print(-1)
    exit()
ans = set()
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            ans.add((i, j))
stack = [(0, 0, 0, set())]
idx = 0
visited = set()
ansval = 2500
check = 0
if not ans:
    ansval = 0
    idx = 1
while idx < len(stack):
    r, c, cnt, basket = stack[idx]
    visited.add((r, c))
    idx += 1
    if r+2 > N-1 or c+2 > M-1 or cnt > ansval:
        continue
    ajbasket = set()
    if ((r,c) not in basket and A[r][c]!=B[r][c])or ((r,c) in basket and A[r][c]==B[r][c]):
        for i in range(3):
            for j in range(3):
                ajbasket.add((r+i, c+j))
        basket = set(basket|ajbasket)-set(basket&ajbasket)
        cnt += 1
    if ans == basket and ansval > cnt:
        ansval = cnt
    if (r+1, c) not in visited and r+3 < N:
        stack.append((r+1, c, cnt, basket))
    elif r+3 >= N and (0, c+1) not in visited and c+3 < M:
        stack.append((0, c+1, cnt, basket))
print(ansval if ansval < 2500 else -1)