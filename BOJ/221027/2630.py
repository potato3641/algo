import sys
from collections import deque
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
board = [list(miis()) for _ in range(N)]
myq = deque()
myq.append((0, 0, N)) # y, x, radius
wcnt, bcnt = 0, 0
while myq:
    y, x, r = myq.popleft()
    if r==1:
        if board[y][x]:
            bcnt += 1
        else:
            wcnt += 1
    else:
        prev = -1
        for i in range(y, y+r):
            if prev == -1:
                prev = sum(board[i][x:x+r])
                if prev not in (r, 0):
                    myq.append((y, x, r//2))
                    myq.append((y+r//2, x, r//2))
                    myq.append((y, x+r//2, r//2))
                    myq.append((y+r//2, x+r//2, r//2))
                    break
            elif prev != sum(board[i][x:x+r]):
                myq.append((y, x, r//2))
                myq.append((y+r//2, x, r//2))
                myq.append((y, x+r//2, r//2))
                myq.append((y+r//2, x+r//2, r//2))
                break
        else:
            if sum(board[y][x:x+r]) == r:
                bcnt += 1
            elif sum(board[y][x:x+r]) == 0:
                wcnt += 1
print(wcnt)
print(bcnt)
