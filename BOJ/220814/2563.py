N = int(input())
line = []
for i in range(N):
    line.append(list(map(int,input().split()))+[10, 10])
rst = 0
for i in range(100):
    coord = [0]*100
    for x in range(N):
        if line[x][1] <= i < line[x][1]+line[x][3]:
            coord[line[x][0]:line[x][0]+line[x][2]] = [1]*line[x][2]
    rst += sum(coord)
print(rst)
