N, M = map(int,input().split())
line = tuple(x for x in range(1, N+1))
answer = []
for i in range(1<<N):
    temp = []
    for j in range(N):
        if i&(1<<j):
            temp.append(line[j])
    if len(temp) == M:
        answer.append(tuple(temp))
answer.sort()
for i in answer:
    print(*i)
