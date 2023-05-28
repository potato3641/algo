N, M = map(int,input().split())
origin = list(map(int,input().split()))
myq = list((x, ) for x in origin)
answer = []
while myq:
    target = myq.pop()
    if len(target) < M:
        for i in origin:
            if i not in target:
                myq.append(target+(i, ))
    else:
        answer.append(target)
answer.sort()
for i in answer:
    print(*i)
