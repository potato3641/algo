K = int(input())
line = []
coord = [(0, 0)]
for i in range(6):
    temp = list(map(int,input().split()))
    line.append(temp)
    if temp[0] == 4:
        coord.append((coord[-1][0],coord[-1][1]+temp[1]))
    elif temp[0] == 3:
        coord.append((coord[-1][0],coord[-1][1]-temp[1]))
    elif temp[0] == 2:
        coord.append((coord[-1][0]-temp[1],coord[-1][1]))
    elif temp[0] == 1:
        coord.append((coord[-1][0]+temp[1],coord[-1][1]))
zip_coord = list(zip(*coord))
max_height, min_height = max(zip_coord[1]), min(zip_coord[1])
max_width, min_width = max(zip_coord[0]), min(zip_coord[0])
rst = (max_height-min_height)*(max_width-min_width)
rst = rst if rst >= 0 else -rst
target = tuple()
if (min_width, max_height) not in coord:
    target = (min_width, max_height)
elif (min_width, min_height) not in coord:
    target = (min_width, min_height)
elif (max_width, max_height) not in coord:
    target = (max_width, max_height)
elif (max_width, min_height) not in coord:
    target = (max_width, min_height)
for x, y in coord:
    if x != target[0] and x != min_width and x != max_width:
        if y != target[1] and y != min_height and y != max_height:
            temp = (target[0]-x)*(target[1]-y)
            temp = temp if temp >= 0 else -temp
            rst -= temp
            break
print(rst*K)
