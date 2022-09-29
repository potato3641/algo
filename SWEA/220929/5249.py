def miis(): return map(int, input().split())
def ii(): return int(input())

def makeset(n):
    global nodict
    nodict[n] = n
def findset(n):
    global nodict
    if nodict[n]!=n:
        nodict[n] = findset(nodict[n])
    return nodict[n]
def unionset(n, m):
    global nodict
    nodict[findset(n)] = m

nodict = dict()
T = ii()
for tc in range(1, T+1):
    V, E = miis()
    board = [list(miis()) for _ in range(E)] # n1, n2, w
    board.sort(key=lambda x:x[2])
    nodict = dict()
    rst = 0
    for i in range(V+1):
        makeset(i)
    for u, v, w in board:
        if findset(u) != findset(v):
            rst += w
            unionset(u, v)
    print(f'#{tc}', rst)
