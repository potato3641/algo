N, M, L = map(int,input().split())
line = [0 for _ in range(N)]
target = 0
line[target] = 1
cnt = 0
while M not in line:
    cnt += 1
    if line[target]%2:
        target += L
        target %= N
    else:
        target -= L
        target %= N
    line[target] += 1
print(cnt)
