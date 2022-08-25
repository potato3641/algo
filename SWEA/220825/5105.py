import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    starting_point = 0
    for i in range(N):
        temp = input()
        if temp.find('2') != -1:
            starting_point = (i, temp.find('2'), 0)
        board.append(list(map(int,list(temp))))
    waiting = [starting_point]
    save_point = []
    cnt = 0
    rst = 0
    while True:
        if waiting:
            y, x, n = waiting.pop(0)
            # q q1 q1 q1 q1 q q2 q2 q2 q2 q2 q2
            if board[y][x] == 3:
                rst = n-1
                break
            board[y][x] = 1
            crs = 0
            if y+1 < N and board[y+1][x] != 1:
                waiting.append((y+1, x, n+1))
                crs += 1
            if y-1 >= 0 and board[y-1][x] != 1:
                waiting.append((y-1, x, n+1))
                crs += 1
            if x+1 < N and board[y][x+1] != 1:
                waiting.append((y, x+1, n+1))
                crs += 1
            if x-1 >= 0 and board[y][x-1] != 1:
                waiting.append((y, x-1, n+1))
                crs += 1
            if not crs:
                continue
        else:
            break
    print(f'#{tc}', rst)