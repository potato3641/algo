import sys
sys.stdin = open('input.txt')
fishing = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
def dfs(visited, n, m):
    
    dfs(visited+[G[fishing[n][m]][0]],n,m)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(3)]
    dfs([], 0, 0)