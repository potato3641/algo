def ewsn(a, b):
    a1, a2 = a
    b1, b2 = b
    if a1+1==b1 and a2==b2:
        return True
    if a1-1==b1 and a2==b2:
        return True
    if a1==b1 and a2+1==b2:
        return True
    if a1==b1 and a2-1==b2:
        return True
    return False
def dfs(visited, sevens):
    for i in range(4):
        for j in range(4):
            if visited:
                if ewsn(visited[-1],(i,j)):
                    if len(visited) == 6:
                        if sevens+board[i][j] not in myseven:
                            myseven.append(sevens+board[i][j])
                    else:
                        dfs(visited+[(i,j)], sevens+board[i][j])
            else:
                dfs(visited+[(i,j)], sevens+board[i][j])
T = int(input())
for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    myseven = []
    dfs([], '')
    print(f'#{tc}', len(myseven))