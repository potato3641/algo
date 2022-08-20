def dfs(board, n):
    #print(n, *temp)
    for i in [x[1] for x in board if x[0] == n]:
        # n번째에서 열 인자 선택
        # board[n][i]
        j = 0
        temp = board[:]
        while True:
            # 해당 열 인자를 가진 값 제거
            if j > len(temp)-1:
                break
            flag = True
            if temp[j][0] == n or temp[j][1] == i or temp[j][0]-n == temp[j][1]-i or temp[j][0]-n == i-temp[j][1]:
                del temp[j]
                flag = False
            if flag: j += 1
        temp.append((n, i))
        if n == N-1:
            global RST
            RST += 1
            return
        if len(temp) < N-n-1:
            return
        else:
            dfs(temp[:], n+1)
RST = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    RST = 0
    for i in range(N):
        for j in range(N):
            board += [(i, j)]
    dfs(board[:], 0)
    print(f'#{tc}', RST)
