N, K = map(int,input().split())
lines = [[0]*2 for _ in range(6)]
for i in range(N):
    line = list(map(int,input().split()))
    lines[line[1]-1][line[0]] += 1
rst = 0
for i in range(6):
    for j in range(2):
        if lines[i][j]:
            rst += (lines[i][j]-1)//K+1
print(rst)
