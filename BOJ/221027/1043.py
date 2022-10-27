import sys
def miis(): return map(int,input().split())
def ii(): return int(input())
N, M = miis()
line = input()
truecnt = 0
trueset = set()
if not line.isnumeric():
    trueset = set(map(int,line.split()[1:]))
    truecnt = len(line)
party = [list(miis()) for _ in range(M)]
partynum = list(range(M))
worked = True
while worked:
    worked = False
    for p in range(len(partynum)-1, -1, -1):
        cnt, *line = party[partynum[p]]
        for i in line:
            if i in trueset:
                trueset |= set(line)
                partynum.remove(partynum[p])
                worked = True
                break
print(len(partynum))
