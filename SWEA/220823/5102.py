def dfs(visited, start, end, n):    # 시작과 끝이 정해진 dfs
    # print(visited, start, end)
    global VAL
    if VAL!=0 and n+1 > VAL: return
    for i in nodes:
        if i not in visited and i[0] == start:
            if i[1]==end:             # 끝났니
                if VAL != 0:
                    VAL = min(VAL, n+1)            # end에 도달 못 하면 실행이 안 됨
                else:
                    VAL = n+1
            else:
                dfs(visited+[(start, i[1]), (i[1], start)], i[1], end, n+1) # 안끝났으면 시작지점을 여기부터
T = int(input())
VAL = 0
for tc in range(1, T+1):
    V, E = map(int,input().split())
    nodes = []
    VAL = 0
    for i in range(E):
        start, end = map(int,input().split())
        nodes.append((start, end))
        nodes.append((end, start))
    S, G = map(int,input().split())
    dfs([], S, G, 0)
    print(f'#{tc}', VAL)