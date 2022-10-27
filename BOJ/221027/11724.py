import sys
input = sys.stdin.readline
def miis(): return map(int,input().split())
def ii(): return int(input())
N, M = miis()
ans = 0
cclist = []
visited = set()
for _ in range(M):
    u, v = miis()
    if u not in visited and v not in visited:
        cclist.append({u, v})
        visited.add(u)
        visited.add(v)
    elif u not in visited and v in visited:
        for cc in cclist:
            if v in cc:
                cc.add(u)
        visited.add(u)
    elif u in visited and v not in visited:
        for cc in cclist:
            if u in cc:
                cc.add(v)
        visited.add(v)
    else:
        U, V = set(), set()
        for cc in range(len(cclist)-1, -1, -1):
            if u in cclist[cc]:
                U = cclist[cc]
                if v in cclist[cc]:
                    break
                del cclist[cc]
            elif v in cclist[cc]:
                V = cclist[cc]
                del cclist[cc]
        else:
            cclist.append(set(U|V))
for i in range(1, N+1):
    if i not in visited:
        cclist.append({i})
print(len(cclist))
