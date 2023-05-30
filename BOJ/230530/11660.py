def minusOne(n): return n-1
N, M = map(int,input().split())
board = list(tuple() for _ in range(N))
answer = []
for i in range(N):
    line = tuple(map(int,input().split()))
    temp = []
    val = 0
    for j in line:
        val += j
        temp.append(val)
    line = tuple(temp)
    if i:
        board[i] = tuple(a+b for a,b in zip(board[i-1],line))
    else:
        board[i] = line
for _ in range(M):
    x1, y1, x2, y2 = map(minusOne,map(int,input().split()))
    if y1 and x1:
        answer.append(board[x2][y2]+board[x1-1][y1-1]-board[x1-1][y2]-board[x2][y1-1])
    elif y1 and not x1:
        answer.append(board[x2][y2]-board[x2][y1-1])
    elif not y1 and x1:
        answer.append(board[x2][y2]-board[x1-1][y2])
    else:
        answer.append(board[x2][y2])
print(*answer, sep='\n')
