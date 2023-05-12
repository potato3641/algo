N, M = map(int,input().split())
marked = []
board = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]:
            marked.append((i, j))
amp = 1

visited = {(0, 0)}
banned = {(0, 0)}
worked = True
while worked:
    worked = False
    for i, j in marked:
        for dy in range(-amp, amp+1):
            for dx in range(-amp, amp+1):
                if (dy, dx) not in visited:
                    visited.add((dy, dx))
                if (dy, dx) not in banned:
                    ny, nx = i+dy, j+dx
                    if 0<=ny<N and 0<=nx<M and (not board[ny][nx] or board[ny][nx] > amp):
                        worked = True
                        board[ny][nx] = amp
    banned |= visited
    amp += 1
print(max(max(x) for x in board))
