M, N = map(int,input().split())
stores = int(input())
coord = []
for i in range(stores+1):
    dir, dist = map(int,input().split())
    coord.append((dir, dist))
dist = 0
dg = coord[-1]
for i in range(stores-1, -1, -1):
    if dg[0] == coord[i][0]:
        dist += abs(coord[i][1] - dg[1])
    elif dg[0] == 1 and coord[i][0] == 2:
        dist += N + min(dg[1] + coord[i][1], M-dg[1] + M-coord[i][1])
    elif dg[0] == 1 and coord[i][0] == 3:
        dist += dg[1] + coord[i][1]
    elif dg[0] == 1 and coord[i][0] == 4:
        dist += M-dg[1] + coord[i][1]
    elif dg[0] == 2 and coord[i][0] == 1:
        dist += N + min(dg[1] + coord[i][1], M-dg[1] + M-coord[i][1])
    elif dg[0] == 2 and coord[i][0] == 3:
        dist += dg[1] + N-coord[i][1]
    elif dg[0] == 2 and coord[i][0] == 4:
        dist += M-dg[1] + N-coord[i][1]
    elif dg[0] == 3 and coord[i][0] == 1:
        dist += dg[1] + coord[i][1]
    elif dg[0] == 3 and coord[i][0] == 2:
        dist += N-dg[1] + coord[i][1]
    elif dg[0] == 3 and coord[i][0] == 4:
        dist += M + min(dg[1] + coord[i][1], N-dg[1] + N-coord[i][1])
    elif dg[0] == 4 and coord[i][0] == 1:
        dist += dg[1] + M-coord[i][1]
    elif dg[0] == 4 and coord[i][0] == 2:
        dist += N-dg[1] + M-coord[i][1]
    elif dg[0] == 4 and coord[i][0] == 3:
        dist += M + min(dg[1] + coord[i][1], N-dg[1] + N-coord[i][1])
print(dist)
