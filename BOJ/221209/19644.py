import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
ML, MK = miis()
BOMB = ii()
board = tuple(ii() for _ in range(N))
BOMBUSED = set()
ans = 'YES'
if BOMB - sum(x > ML*MK for x in board) < 0:
    BOMB = -1
else:
    for i in range(N):
        BOMBUSED.discard(i)
        if i < ML-1:
            if board[i]-(i+1-len(BOMBUSED))*MK > 0:
                BOMB -= 1
                BOMBUSED.add(i+ML)
        else:
            if board[i]-(ML-len(BOMBUSED))*MK > 0:
                BOMB -= 1
                BOMBUSED.add(i+ML)
        if BOMB < 0:
            break
if BOMB < 0:
    ans = 'NO'
print(ans)
