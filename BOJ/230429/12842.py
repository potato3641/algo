N, S = map(int,input().split())
M = int(input())
tline = sorted(list((int(input()), idx) for idx in range(M)), key=lambda x: (x[1], x[0]))
limit = N-S
timer = 0
cnt = 0
answer = -1
stay = set()
while cnt < limit:
    for i in range(M):
        if timer%tline[i][0]==0:
            cnt += 1
            if cnt == limit:
                answer = tline[i][1]+1
                break
    timer += 1
print(answer)
