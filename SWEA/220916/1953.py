def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = miis()
    board = [list(miis()) for _ in range(N)]
    myq = []
    visited = []
    myq.append((R, C, 1))
    visited.append((R, C))
    upp = [1,2,4,7]
    downn = [1,2,5,6]
    rightt = [1,3,4,5]
    leftt = [1,3,6,7]
    while len(myq):
        target = myq.pop(0)
        y, x, dist = target
        if board[y][x] in upp and y-1 >= 0 and board[y-1][x] in downn and dist < L:
            if (y-1, x) in visited:
                temp = [qs for qs in myq if qs[0]==y-1 and qs[1]==x]
                if len(temp):
                    if temp[0][2] > dist+1:
                        myq.remove((y-1, x, temp[0][2]))
                        myq.append((y-1, x, dist+1))
            else:
                visited.append((y-1, x))
                myq.append((y-1, x, dist+1))
        if board[y][x] in downn and y+1 < N and board[y+1][x] in upp and dist < L:
            if (y+1, x) in visited:
                temp = [qs for qs in myq if qs[0]==y-1 and qs[1]==x]
                if len(temp):
                    if temp[0][2] > dist+1:
                        myq.remove((y+1, x, temp[0][2]))
                        myq.append((y+1, x, dist+1))
            else:
                visited.append((y+1, x))
                myq.append((y+1, x, dist+1))
        if board[y][x] in leftt and x-1 >= 0 and board[y][x-1] in rightt and dist < L:
            if (y, x-1) in visited:
                temp = [qs for qs in myq if qs[0]==y-1 and qs[1]==x]
                if len(temp):
                    if temp[0][2] > dist+1:
                        myq.remove((y, x-1, temp[0][2]))
                        myq.append((y, x-1, dist+1))
            else:
                visited.append((y, x-1))
                myq.append((y, x-1, dist+1))
        if board[y][x] in rightt and x+1 < M and board[y][x+1] in leftt and dist < L:
            if (y, x+1) in visited:
                temp = [qs for qs in myq if qs[0]==y-1 and qs[1]==x]
                if len(temp):
                    if temp[0][2] > dist+1:
                        myq.remove((y, x+1, temp[0][2]))
                        myq.append((y, x+1, dist+1))
            else:
                visited.append((y, x+1))
                myq.append((y, x+1, dist+1))
        # viewer
        # for i in range(N):
        #     for j in range(M):
        #         if i==R and j==C:
        #             print('1',end='')
        #         elif (i, j) in visited:
        #             print('0',end='')
        #         else:
        #             print(mytest[board[i][j]],end='')
        #     print()
    print(f'#{tc}', len(visited))

