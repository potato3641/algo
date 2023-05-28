A, B = map(int,input().split())
myq = [(A, 1)]
mincnt = float('inf')
while myq:
    target, cnt = myq.pop()
    if cnt >= mincnt:
        break
    if target*2 < B:
        myq.append((target*2, cnt+1))
    elif target*2 == B:
        if mincnt > cnt+1:
            mincnt = cnt+1
    if target*10+1 < B:
        myq.append((target*10+1, cnt+1))
    elif target*10+1 == B:
        if mincnt > cnt+1:
            mincnt = cnt+1
if mincnt == float('inf'):
    print(-1)
else:
    print(mincnt)
