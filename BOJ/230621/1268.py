N = int(input())
board = tuple(tuple(map(int,input().split())) for _ in range(N))
revboard = tuple(map(tuple,zip(*board)))
maxlen = -1
maxidx = -1
for ts in range(N): # target student
    basket = set()
    for i in range(5):
        temp = set(x for x in range(len(revboard[i])) if revboard[i][x] == revboard[i][ts])
        temp.discard(ts)
        basket |= temp
    if maxlen < len(basket):
        maxlen = len(basket)
        maxidx = ts
print(maxidx+1)