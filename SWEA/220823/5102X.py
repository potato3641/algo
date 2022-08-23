import sys
sys.stdin = open('input.txt')

def dfs(nodes, start, end, n):    # 시작과 끝이 정해진 dfs
    for i in range(1, len(nodes)):
        if nodes[i] not in nodes[0] and nodes[i][0] == start:
            if nodes[i][1]==end:             # 끝났니
                global VAL         # 사실 매개변수 자리로 보내도 됨
                if VAL != 0:
                    VAL = min(VAL, n+1)            # end에 도달 못 하면 실행이 안 됨
                else:
                    VAL = n+1
            else:
                nodes[0].append((start, nodes[i][1]))
                nodes[0].append((nodes[i][1], start))
                dfs(nodes, nodes[i][1], end, n+1) # 안끝났으면 시작지점을 여기부터
                nodes[0].remove((start, nodes[i][1]))
                nodes[0].remove((nodes[i][1], start))
T = int(input())
VAL = 0
for tc in range(1, T+1):
    V, E = map(int,input().split())
    nodes = [[]]
    VAL = 0
    for i in range(E):
        start, end = map(int,input().split())
        nodes.append((start, end))
        nodes.append((end, start))
    S, G = map(int,input().split())
    dfs(nodes, S, G, 0)
    print(f'#{tc}', VAL)