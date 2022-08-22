line = []
for i in range(4):
    line.append(list(map(int,input().split())))
rst = 0
for i in range(100):
    coord = [0]*100
    for x in range(4):
        if line[x][1] <= i < line[x][3]:
            coord[line[x][0]:line[x][2]] = [1]*(line[x][2]-line[x][0])
    rst += sum(coord)
print(rst)
