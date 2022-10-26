from collections import deque
N=int(input())
M=int(input())
board = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    board[s].append(e)
    board[e].append(s)
visited = {1}
myq = deque()
myq.append(1)
while myq:
    target = myq.popleft()
    for i in board[target]:
        if i not in visited:
            myq.append(i)
            visited.add(i)
print(len(visited)-1)
