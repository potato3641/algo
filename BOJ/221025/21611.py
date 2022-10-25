import sys
input = sys.stdin.readline
def miis(): return map(int,input().split())
def ii(): return int(input())
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
myidx = (7, 3, 1, 5)
N, M = miis()
board = [list(miis()) for _ in range(N)]
orders = [tuple(miis()) for _ in range(M)]
marble = ['shark']
sharkpos = ((N-1)//2, (N-1)//2)
d = 2
y, x = sharkpos
visited = {(y, x)}
while 0<=y+dy[d]<N and 0<=x+dx[d]<N:
    y, x = y+dy[d], x+dx[d]
    visited.add((y, x))
    if board[y][x]:
        marble.append(board[y][x])
        d = (d-1)%4
        if (y+dy[d], x+dx[d]) in visited:
            d = (d+1)%4
    else:
        break
ans = 0
# 1. 얼음던져!
for d, s in orders:
# 2. 타겟 찾아서 파괴
    initval = myidx[d-1]
    # a*cnt+a*(a-1)*4
    for i in range(s, 0, -1):
        if initval*i+i*(i-1)*4 < len(marble):
            del marble[initval*i+i*(i-1)*4]
    # 3. under 2 while
    while True:
    # 3-1. 땡겨(자동화됨)
    # 3-2. 같은거 폭발
        prev = None
        targetidx = set()
        tempidx = set()
        cnt = 0
        for i in range(len(marble)):
            if marble[i]==prev:
                cnt += 1
                tempidx.add(i-1)
                tempidx.add(i)
            else:
                if cnt >= 3:
                    targetidx |= tempidx
                tempidx = set()
                cnt = 0
            prev = marble[i]
        else:
            if cnt >= 3:
                targetidx |= tempidx
        if not targetidx:
            break
        else:
            for i in sorted(list(targetidx),reverse=True):
                ans += marble[i]
                del marble[i]
    # 4. 그룹만들어서 구슬 복사
    newmarble = ['shark']
    prev = 'shark'
    cnt = 1
    lastworked = False
    for i in range(1, len(marble)):
        lastworked = False
        if marble[i] == prev:
            cnt += 1
        else:
            if prev != 'shark':
                newmarble.append(cnt)
                newmarble.append(marble[i-1])
            cnt = 1
            lastworked = True
        prev = marble[i]
        if len(newmarble) > N*N:
            break
    else:
        if marble[i-1] != 'shark':
            newmarble.append(cnt)
            if lastworked:
                newmarble.append(marble[i])
            else:
                newmarble.append(marble[i-1])
    marble = newmarble[:N*N]
    # print(marble, len(marble))
print(ans)
