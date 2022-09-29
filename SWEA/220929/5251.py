from math import inf
import sys
sys.stdin = open('input.txt')
def miis(): return map(int, input().split())
def ii(): return int(input())

T = ii()
for tc in range(1, T+1):
    N, E = miis()
    prim = [[inf]*(N+1) for _ in range(N+1)]
    dist = [inf]*(N+1)
    dist[0] = 0
    visited = [False]*(N+1)
    for _ in range(E):
        s, e, w = miis()
        prim[s][e] = w
    for _ in range(N+1):
        min_idx = -1
        min_value = inf
        for i in range(N+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True
        for i in range(N+1):
            if not visited[i] and prim[min_idx][i]+dist[min_idx] < dist[i]:
                dist[i] = prim[min_idx][i] + dist[min_idx]
        # print(visited, dist)
                
    print(f'#{tc}', dist[N])
