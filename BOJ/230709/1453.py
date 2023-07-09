N = int(input())
board = [False for _ in range(101)]
cnt = 0
for i in map(int,input().split()):
    if not board[i]:
        board[i] = True
    else:
        cnt += 1
print(cnt)
