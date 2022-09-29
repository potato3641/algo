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
    line = list(miis())
    board = []
    for i in range(len(line)//2):
        board.append((line[i*2],line[i*2+1]))
    nodict = dict()
    rst = 0
    for i in range(1, V+1):
        makeset(i)
    for u, v in board:
        if findset(u) != findset(v):
            unionset(u, v)
    bossdict = dict()
    for i in nodict:
        temp = findset(i)
        if temp not in bossdict:
            bossdict[temp] = 1
        else:
            bossdict[temp] += 1
    print(f'#{tc}', len(bossdict))
