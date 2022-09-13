def addray(A, B):
    for i in range(N):
        if B[i]:
            A[i] = 1
    return A, B
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
new_board = [0]*N
for i in range(N):
    new_board[i] = board[i][:]
    myq = []
    visited = []
    for j in range(N):
        if board[i][j]:
            myq.append(j)
            visited.append(j)
    while len(myq):
        target = myq[-1]
        del myq[-1]
        new_board[i], board[target] = addray(new_board[i], board[target])
        for j in range(N):
            if board[target][j]:
                if j not in visited:
                    visited.append(j)
                    myq.append(j)
for i in range(N):
    print(*new_board[i])
