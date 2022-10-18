def getline():
    return input().split()
def dfs(cur, gx, gy, visited):
    for i in board[cur]:
        if i not in visited:
            if (cur, i) in nodict:
                x, y = nodict[(cur, i)]
            else:
                x, y = nodict[(i, cur)]
            global min_val
            if i == 2:
                now_val = (gx+x)*(gy+y)
                if min_val > now_val:
                    min_val = now_val
                continue
            if (gx+x)*(gy+y) < min_val:
                dfs(i, gx+x, gy+y, visited+[i])
min_val = float('inf')
T = int(input())
buffer = 0
for tc in range(1, T+1):
    buffer = getline()
    try:
        N, M = map(int, buffer)
    except:
        N, M = map(int, getline())
    if M == 0:
        print(f'#{tc}', -1)
        continue
    board = [[] for _ in range(N+1)]
    nodict = dict()
    for _ in range(M):
        a, b, x, y = map(int,input().split())
        board[a].append(b)
        board[b].append(a)
        nodict[(a, b)] = (x, y)
    min_val = float('inf')
    if len(board[2]) == 0:
        print(f'#{tc}', -1)
        continue
    dfs(1, 0, 0, [1])
    if type(min_val) == type(0.0):
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', min_val)
