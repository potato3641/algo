bingo_board = []
bingo_set = [set() for _ in range(12)]
bingo_rst = []
for i in range(5):
    line = list(map(int,input().split()))
    bingo_board.append(line)
    bingo_set[i] = set(line)
i = 0
for j in zip(*bingo_board):
    bingo_set[5+i] = set(j)
    bingo_set[10].add(bingo_board[i][i])
    bingo_set[11].add(bingo_board[i][4-i])
    i += 1
cnt = 0
for _ in range(5):
    for i in list(map(int,input().split())):
        bingo_rst.append(i)
        cnt += 1
        rst = 0
        for j in bingo_set:
            if len(j - set(bingo_rst)) == 0:
                rst += 1
                if rst > 2:
                    break
        if rst > 2:
            break
    if rst > 2:
        break
print(cnt)
