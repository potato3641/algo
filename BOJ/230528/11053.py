N = int(input())
line = tuple(map(int,input().split()))
myq = [(x, 1) for x in range(N)]
vals = [0 for _ in range(N)]
while myq:
    idx, cnt = myq.pop()
    for i in range(idx+1, N):
        if line[i] > line[idx] and vals[i] < cnt+1:
            vals[i] = cnt+1
            myq.append((i, cnt+1))
answer = max(vals)
if answer:
    print(answer)
else:
    print(1)