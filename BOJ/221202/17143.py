def miis(): return map(int,input().split())
def ii(): return int(input())
N, M, K = miis()
dy = (-1, 1, 0, 0)
dx = (0, 0, 1, -1)
revDir = (1, 0, 3, 2)
sharkinfo = [] # y, x, v, d, s
for _ in range(K):
    y, x, v, d, s = miis()
    y -= 1
    x -= 1
    d -= 1
    sharkinfo.append((y, x, v, d, s))
def gotcha(n):
    target = -1
    target_y = N
    target_s = 0
    for i in range(len(sharkinfo)):
        y, x, v, d, s = sharkinfo[i]
        if x==n and y < target_y:
            target_y = y+0
            target_s = s+0
            target = i+0
    if target == -1:
        return 0
    else:
        del sharkinfo[target]
        return target_s
def sharkmove():
    for i in range(len(sharkinfo)):
        y, x, v, d, s = sharkinfo[i]
        if d < 2:
            y = (y+dy[d]*v) % ((N-1)*2)
            if y > N-1:
                dist = y-N+1
                y = N-1-dist
                d = revDir[d]
        else:
            if v > 0:
                x = (x+dx[d]*v) % ((M-1)*2)
                if x > M-1:
                    dist = x-M+1
                    x = M-1-dist
                    d = revDir[d]
        sharkinfo[i] = (y, x, v, d, s)
def sharkate():
    codict = dict()
    lenshark = len(sharkinfo)
    for i in range(lenshark-1, -1, -1):
        y, x, v, d, s = sharkinfo[i]
        if (y, x) not in codict:
            codict[(y, x)] = (s+0, sharkinfo[i])
        else:
            prevs, infos = codict[(y, x)]
            if prevs < s:
                sharkinfo.remove(infos)
                codict[(y, x)] = (s+0, sharkinfo[i])
            else:
                sharkinfo.remove(sharkinfo[i])
ans = 0
# 꾼 이동 - for
for c in range(M):
    if len(sharkinfo)==0:
        break
# 상어잡이 - def
    ans += gotcha(c)
# 상어 이동 - def
    sharkmove()
    sharkinfo.sort(key=lambda x: x[4], reverse=True)
# 상어포식 - def
    sharkate()
print(ans)
