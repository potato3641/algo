N = int(input())
line = []
for i in range(N):
    line.append(list(map(int,input().split())))
rst = [0]*N
for i in range(1001):
    coord = [-1]*1001
    for x in range(N):
        if line[x][1] <= i < line[x][1]+line[x][3]:
            coord[line[x][0]:line[x][0]+line[x][2]] = [x]*line[x][2]
    for x in range(N):
        rst[x] += coord.count(x)
for x in range(N):
    print(rst[x])
