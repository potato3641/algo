from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# cycle :
debugger = False
ans = 0
while True:
    # find max block group
    ifoundit = set()
    targetgroup = set()
    max_val = 0
    max_rain = 0
    max_row = -1
    max_col = -1
    for i in range(N):
        for j in range(N):
            if (i, j) not in ifoundit and board[i][j] is not None and board[i][j] > 0:
                myq = deque()
                myq.append((i, j))
                visited = set()
                while len(myq):
                    y, x = myq.popleft()
                    visited.add((y, x))
                    for d in range(4):
                        if (y+dy[d], x+dx[d]) not in visited:
                            if 0<=y+dy[d]<N and 0<=x+dx[d]<N:
                                if board[y+dy[d]][x+dx[d]] in (0, board[i][j]):
                                    myq.append((y+dy[d], x+dx[d]))
                                    visited.add((y+dy[d], x+dx[d]))
                                    ifoundit.add((y+dy[d], x+dx[d]))
                rain_cnt = sum(0 if board[y][x]==0 else 1 for y, x in visited)
                if rain_cnt==0 or len(visited) < 2:
                    continue
                rain_cnt = len(visited)-rain_cnt
                if max_val < len(visited):
                    max_val = len(visited)
                    max_rain = rain_cnt
                    max_row = i
                    max_col = j
                    targetgroup = set(visited)
                elif max_val == len(visited):
                    if max_rain < rain_cnt:
                        max_rain = rain_cnt
                        max_row = i
                        max_col = j
                        targetgroup = set(visited)
                    elif max_rain == rain_cnt:
                        if max_row < i:
                            max_row = i
                            max_col = j
                            targetgroup = set(visited)
                        elif max_row == i:
                            if max_col < j:
                                max_col = j
                                targetgroup = set(visited)
    if debugger: print(targetgroup)
    # delete and get point
    if len(targetgroup) < 2:
        break
    for y, x in targetgroup:
        board[y][x] = None
    ans += len(targetgroup)**2
    if debugger: print(ans)
    todo = False
    for i in range(N):
        for j in range(N):
            if board[i][j] not in (-1, None):
                todo = True
                break
        if todo:
            break
    else:
        # print(ans)
        break
    # if debugger: print(board)
    # underset\
    for j in range(N):
        for i in range(N-1,0,-1):
            if board[i][j] is None:
                cnt = -1
                while i+cnt > 0 and board[i+cnt][j] is None:
                    cnt -= 1
                if board[i+cnt][j] not in (None, -1):
                    board[i][j] = board[i+cnt][j]
                    board[i+cnt][j] = None
    # if debugger: print(board)
    # rotate
    temp = [[None]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[N-j-1][i] = board[i][j]
    # if debugger: print(temp)
    board = temp
    # underset
    for j in range(N):
        for i in range(N-1,0,-1):
            if board[i][j] is None:
                cnt = -1
                while i+cnt > 0 and board[i+cnt][j] is None:
                    cnt -= 1
                if board[i+cnt][j] not in (None, -1):
                    board[i][j] = board[i+cnt][j]
                    board[i+cnt][j] = None
    if debugger: print(board)
print(ans)
