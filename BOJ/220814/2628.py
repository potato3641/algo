X, Y = map(int,input().split())
N = int(input())
cutter = [[0, Y], [0, X]]
for i in range(N):
    bool_xy, num_xy = map(int,input().split())
    cutter[bool_xy].append(num_xy)
cutter[0].sort()
cutter[1].sort()
rst = 0
for i in range(len(cutter[0])-1):
    for j in range(len(cutter[1])-1):
        temp = (cutter[0][i+1]-cutter[0][i])*(cutter[1][j+1]-cutter[1][j])
        rst = max(rst,temp)
print(rst)
