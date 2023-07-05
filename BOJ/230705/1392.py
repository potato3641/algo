N, Q = map(int,input().split())
ackbo = list(int(input()) for _ in range(N))
basedict = dict()
cnt = 0
for i in range(sum(ackbo)):
    basedict[i] = cnt+1
    ackbo[cnt] -= 1
    if not ackbo[cnt]:
        cnt += 1
for _ in range(Q):
    print(basedict[int(input())])
