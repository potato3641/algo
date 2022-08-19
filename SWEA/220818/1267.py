T = 10
for tc in range(1, T+1):
    V, E = map(int,input().split())
    line = list(map(int,input().split()))
    board = [[] for _ in range(V+1)]
    youneed = [[] for _ in range(V+1)]
    for i in range(E):
        board[line[i*2]].append(line[i*2+1])
        youneed[line[i*2+1]].append(line[i*2])
    flag = True
    while flag:
        for i in range(1,V+1):
            if not youneed[i] and i not in board[0]:
                board[0].append(i)
                for j in board[i]:
                    youneed[j].remove(i)
                board[i] = []
                break
        else:
            flag = False
    print(f'#{tc}', *board[0])
