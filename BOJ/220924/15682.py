def miis(): return map(int,input().split())
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
def generco(y, x, curved):
    rst = {(y, x)}
    prevY = y
    prevX = x
    for i in curved:
        prevY += dy[i]
        prevX += dx[i]
        rst.add((prevY, prevX))
    return rst
N = int(input())
# x y d g
curboard = [list(miis()) for _ in range(N)]
# normal[::-1]+1
coboard = []
rst = set()
for x, y, d, g in curboard:
    curved = [d]
    for _ in range(g):
        recurved = curved[::-1]
        for i in recurved:
            curved.append((i+1)%4)
    temp = generco(y, x, curved)
    # print(temp)
    rst |= temp
ans = 0
# print(rst)
for i in range(100):
    for j in range(100):
        if (i, j) in rst and (i+1, j) in rst and (i, j+1) in rst and (i+1, j+1) in rst:
            ans += 1
    #     if (i, j) in rst:
    #         print('1', end='')
    #     else:
    #         print('0',end='')
    # print()

print(ans)
