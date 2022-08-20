def dfs(nodes, start, end):
    for i in nodes[start]:
        if i==end:
            global VAL
            VAL = 1
        else:
            dfs(nodes, i, end)
T = int(input())
VAL = 0
for tc in range(1, T+1):
    V, E = map(int,input().split())
    nodes = [[] for _ in range(V+1)]
    VAL = 0
    for i in range(E):
        start, end = map(int,input().split())
        nodes[start].append(end)
    S, G = map(int,input().split())
    dfs(nodes, S, G)
    if VAL:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
