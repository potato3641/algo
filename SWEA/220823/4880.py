def rcs(a, b):
    if line[a] == line[b]:
        return a
    if line[a] == 1:
        if line[b] == 2:
            return b
        else:
            return a
    if line[a] == 2:
        if line[b] == 1:
            return a
        else:
            return b
    if line[a] == 3:
        if line[b] == 1:
            return b
        else:
            return a
def dfs(s, e):
    if len(line[s:e+1]) == 1:
        return s
    if len(line[s:e+1]) == 2:
        return rcs(s, s+1)
    else:
        cutter = (s+e)//2
        return rcs(dfs(s, cutter), dfs(cutter+1, e))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int,input().split()))
    s, e = 0, len(line)-1
    print(f'#{tc}', dfs(s, e)+1)