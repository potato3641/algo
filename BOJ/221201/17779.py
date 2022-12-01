def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
board = [list(miis()) for _ in range(N)]
def five(y, x, d1, d2):
    updy = 0
    downdy = 0
    for dx in range(d1+d2+1):
        if dx >= d1:
            dyDOWN = y-d1+downdy
            downdy += 1
        else:
            dyDOWN = y - dx 
        if dx >= d2:
            dyUP = y+d2-updy
            updy += 1
        else:
            dyUP = y + dx
        for dy in range(dyDOWN, dyUP+1):
            fives.add((dy, x+dx))
def four(y, x, d1, d2):
    rst = 0
    for i in range(y-d1+d2+1, N):
        for j in range(x+d2, N):
            if (i, j) not in fives:
                rst += board[i][j]
    return rst
def three(y, x, d1, d2):
    rst = 0
    for i in range(y, N):
        for j in range(x+d2):
            if (i, j) not in fives:
                rst += board[i][j]
    return rst
def two(y, x, d1, d2):
    rst = 0
    for i in range(y-d1+d2+1):
        for j in range(x+d1+1, N):
            if (i, j) not in fives:
                rst += board[i][j]
    return rst
def one(y, x, d1, d2):
    rst = 0
    for i in range(y):
        for j in range(x+d1+1):
            if (i, j) not in fives:
                rst += board[i][j]
    return rst
minans = float('inf')
for i in range(1, N-1):
    for j in range(1, N-1):
        for d1 in range(1, N):
            if 0<=i+d1<N and 0<=i-d1<N:
                for d2 in range(1, N):
                    if 0<=j+d1+d2<N and 0<=i+d2<N and 0<=i-d2<N:
                        fives = set()
                        five(i, j, d1, d2)
                        fours = four(i, j, d1, d2)
                        threes = three(i, j, d1, d2)
                        twos = two(i, j, d1, d2)
                        ones = one(i, j, d1, d2)
                        fives = sum(board[y][x] for y, x in fives)
                        ans = max(fives, fours, threes, twos, ones)-min(fives, fours, threes, twos, ones)
                        if minans > ans:
                            minans = ans
print(minans)
