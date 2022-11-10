def miis(): return map(int,input().split())
def ii(): return int(input())
def minusOne(n): return n-1
def pushSmell():
    for i in sharkDict:
        sharkSmell[sharkDict[i]] = K
        sharkWhoseSmell[sharkDict[i]] = i+0
def sharkMove():
    sharks = sorted(list(sharkDict.keys()))
    for k in sharks:
        y, x = sharkDict[k]
        sharkOrder = sharkOrders[k][sharkDir[k]]
        for d in sharkOrder:
            if 0<=y+dy[d]<N and 0<=x+dx[d]<N:
                if (y+dy[d], x+dx[d]) not in sharkSmell:
                    if (y+dy[d], x+dx[d]) not in sharkDict.values():
                        sharkDir[k] = d+0
                        sharkDict[k] = (y+dy[d], x+dx[d])
                        break
                    else:
                        del sharkDict[k]
                        break
        else:
            for d in sharkOrder:
                if 0<=y+dy[d]<N and 0<=x+dx[d]<N:
                    if (y+dy[d], x+dx[d]) in sharkSmell:
                        if sharkWhoseSmell[(y+dy[d], x+dx[d])] == k:
                            sharkDir[k] = d+0
                            sharkDict[k] = (y+dy[d], x+dx[d])
                            break
def removeSmell():
    smellKeys = tuple(sharkSmell.keys())
    for i in smellKeys:
        sharkSmell[i] -= 1
        if sharkSmell[i] <= 0:
            del sharkSmell[i]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
N, M, K = miis()
board = tuple(tuple(miis()) for _ in range(N))
sharkDir = list(map(minusOne,miis()))
sharkOrders = tuple(tuple(tuple(map(minusOne,miis())) for _ in range(4)) for _ in range(M))
sharkDict = dict()
sharkSmell = dict()
sharkWhoseSmell = dict()
for i in range(N):
    for j in range(N):
        if board[i][j]:
            sharkDict[board[i][j]-1] = (i, j)
timer = 0
pushSmell()
while timer<=1000:
    sharkMove()
    removeSmell()
    pushSmell()
    timer += 1
    if len(sharkDict) < 2:
        break
if timer > 1000:
    timer = -1
print(timer)
