import sys
input = sys.stdin.readline
N = int(input())
board = [tuple(map(int,input().split())) for _ in range(N)]
board.sort(key=lambda x: x[1], reverse=True)
cnt = 1
max_s, max_e = max(board, key=lambda x: x[1])
for s, e in board:
    if e <= max_s:
        max_s, max_e = s, max_s
        cnt += 1
    elif e <= max_e:
        if max_s < s:
            max_s = s
print(cnt)
