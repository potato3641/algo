N, M = map(int,input().split())
origin = list(map(int,input().split()))
myq = list(((origin[idx], ), (idx, )) for idx in range(len(origin)))
answer = set()
while myq:
    target, idxx = myq.pop()
    if len(target) < M:
        for i in range(len(origin)):
            if i not in idxx:
                myq.append((target+(origin[i], ), (idxx+(i, ))))
    else:
        answer.add(target)
answer = sorted(list(answer))
for i in answer:
    print(*i)
