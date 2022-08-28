N, M, D = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
max_rst = 0
for b0 in range(M):
    for b1 in range(b0+1, M):
        for b2 in range(b1+1, M):
            bower = [b0, b1, b2]
            rst = set()
            for bower_row in range(N, -1, -1):
                b0flag = True
                b1flag = True
                b2flag = True
                temp = set()
                for d in range(1, D+1):
                    b0temp = set()
                    b1temp = set()
                    b2temp = set()
                    for i in range(bower_row-1,-1,-1):
                        for j in range(M):
                            if board[i][j]:
                                if b0flag and abs(i-bower_row)+abs(j-bower[0]) <= d:
                                    b0temp.add((i, j))
                                if b1flag and abs(i-bower_row)+abs(j-bower[1]) <= d:
                                    b1temp.add((i, j))
                                if b2flag and abs(i-bower_row)+abs(j-bower[2]) <= d:
                                    b2temp.add((i, j))
                    if len(b0temp):
                        b0flag = False
                        temp.add(sorted(list(b0temp), key=lambda x:x[1])[0])
                    if len(b1temp):
                        b1flag = False
                        temp.add(sorted(list(b1temp), key=lambda x:x[1])[0])
                    if len(b2temp):
                        b2flag = False
                        temp.add(sorted(list(b2temp), key=lambda x:x[1])[0])
                    if not (b0flag + b1flag + b2flag):
                        break
                for i, j in temp:
                    board[i][j] = 0
                rst |= temp
            if max_rst < len(rst):
                max_rst = len(rst)
            for i, j in rst:
                board[i][j] = 1
print(max_rst)
