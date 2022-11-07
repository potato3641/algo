from collections import deque
def miis(): return map(int,input().split())
def ii(): return int(input())
def adderm1(n):
    return n-1
mv = (-4, -5, -1, 3, 4, 5, 1, -3)
fishdict = [[] for _ in range(16)]
cnt = 0
for _ in range(4):
    line = tuple(map(adderm1, miis()))
    for i in range(4):
        fishdict[cnt] = (line[i*2], line[i*2+1])
        cnt += 1
myq = deque()
# 최초 먹기
sharkloc = 0
sharkval, sharkdir = fishdict[sharkloc]
fishdict[0] = (-1, -1)
maxnum = 0
maxvisit = []
myq.append((sharkloc, sharkdir, [sharkval], fishdict[:]))
while myq:
    loc, dir, visited, board = myq.popleft()
    nownum = sum(visited)+len(visited)
    if maxnum < nownum:
        maxnum = nownum
        maxvisit = visited[:]
# 이동
    for i in range(16):
        if i not in visited:
            targetidx = next(x for x in range(16) if board[x][0] == i)
            sharkval, sharkdir = board[targetidx]
            cnt = 0
            while targetidx+mv[(sharkdir+cnt)%8]<0 or targetidx+mv[(sharkdir+cnt)%8]>15 or targetidx+mv[(sharkdir+cnt)%8]==loc or abs((targetidx+mv[(sharkdir+cnt)%8])%4-targetidx%4) > 1:
                cnt += 1
                if cnt > 7:
                    break
            if cnt < 8:
                gotoidx = targetidx+mv[(sharkdir+cnt)%8]
                sharkval, sharkdir = board[targetidx]
                board[targetidx] = sharkval, (sharkdir+cnt)%8
                board[gotoidx], board[targetidx] = board[targetidx], board[gotoidx]
# 먹기
    cnt = 1
    prevloc = loc%4
    while not (loc+mv[dir]*cnt<0 or loc+mv[dir]*cnt>15 or abs((loc+mv[dir]*cnt)%4-prevloc%4) > 1):
        if board[loc+mv[dir]*cnt] == (-1, -1):
            prevloc = loc+mv[dir]*cnt
            cnt += 1
            continue
        fishval, fishdir = board[loc+mv[dir]*cnt]
        temp = board[:]
        temp[loc+mv[dir]*cnt] = (-1, -1)
        myq.append((loc+mv[dir]*cnt, fishdir, visited+[fishval], temp))
        prevloc = loc+mv[dir]*cnt
        cnt += 1
print(maxnum)
