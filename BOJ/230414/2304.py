def miis(): return map(int,input().split())
N = int(input())
board = [tuple(miis()) for _ in range(N)]
boardict = dict()
for idx, height in board:
    boardict[idx] = height
answer = 0
maxheight = 0
minidx = min(x[0] for x in board)
maxidx = max(x[0] for x in board)
for idx in range(minidx, maxidx+1):
    if idx in boardict:
        height = boardict[idx]
        if maxheight < height:
            maxheight = height
    answer += maxheight
riheight = 0
for idx in range(maxidx, minidx-1, -1):
    if idx in boardict:
        height = boardict[idx]
        if riheight < height:
            riheight = height
    if maxheight == riheight:
        break
    answer -= (maxheight-riheight)
print(answer)
