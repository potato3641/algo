def dfs(brdict, used, completed):
    for i in range(6):
        hap = 0
        if i in completed:
            continue
        for y, x in line[i]:
            if brdict[(y, x)] in alphaset:
                hap += alphastr.index(brdict[(y, x)])
            else:
                for j in alphaset-used:
                    tmpdict = brdict.copy()
                    tmpdict[(y, x)] = j
                    dfs(tmpdict, set(used|{j}), completed)
                return
        else:
            if hap == 26:
                dfs(brdict, used, completed+[i])
            return
    global rst
    rst.append(brdict)
# main
alphastr = ' ABCDEFGHIJKL'
alphaset = set(list('ABCDEFGHIJKL'))
board = [list(input()) for _ in range(5)]
line = [[] for _ in range(6)]
line[0] = [(0, 4), (1, 5), (2, 6), (3, 7)]
line[1] = [(0, 4), (1, 3), (2, 2), (3, 1)]
line[2] = [(3, 1), (3, 3), (3, 5), (3, 7)]
line[3] = [(4, 4), (3, 3), (2, 2), (1, 1)]
line[4] = [(4, 4), (3, 5), (2, 6), (1, 7)]
line[5] = [(1, 1), (1, 3), (1, 5), (1, 7)]
used = set()
brdict = dict()
for i in range(6):
    for y, x in line[i]:
        if board[y][x] != '.':
            if board[y][x] != 'x':
                used.add(board[y][x])
                brdict[(y, x)] = board[y][x]
            else:
                brdict[(y, x)] = 0
rst = []
fstidx = 0
fststr = ''
dfs(brdict, used, [])
cnt = 0
for tmpdict in rst:
    temp = list(tmpdict.keys())
    temp.sort(key=lambda x:(x[0], x[1]))
    tmpstr = ''
    for y, x in temp:
        tmpstr += tmpdict[y, x]
    if fststr == '' or fststr > tmpstr:
        fststr = tmpstr
        fstidx = cnt
    cnt += 1
rst = rst[fstidx]
for i in range(5):
    for j in range(9):
        if (i, j) in rst:
            print(rst[(i, j)], end='')
        else:
            print(board[i][j], end='')
    print()
