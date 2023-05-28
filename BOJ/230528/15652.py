N, M = map(int,input().split())
myq = list((x, ) for x in range(1, N+1))
answer = []
while myq:
    target = myq.pop()
    if len(target) < M:
        for i in range(target[-1], N+1):
            myq.append(target+(i, ))
    else:
        answer.append(target)
answer.sort()
for i in answer:
    print(*i)
