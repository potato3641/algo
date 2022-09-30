from collections import deque
def miis(): return map(int, input().split())
def ii(): return int(input())
def nextbee(y, x):
    addx = 0
    addy = 0
    result = []
    while y+addy != N:
        addx += 1
        if x+addx+M-1 >= N:
            x = 0
            addx = 0
            addy += 1
        if y+addy == N:
            break
        result.append((y+addy, x+addx))
    return result
T = ii()
for tc in range(1, T+1):
    N, M, C = miis()
    board = [list(miis()) for _ in range(N)]
    myq = deque()
    max_honey = 0
    # if tc!=6: continue
    for y, x in nextbee(0, -1):
        myq.append((y, x, 0)) # row col
    while myq:
        y, x, honey = myq.popleft()
        cutter = C+0
        flag = False
        prevH = 0
        if honey:
            prevH = honey+0
            flag = True
        # print(y, x, x+M)
        honey_temp = 0
        for i in range(1<<M):
            temp = []
            for j in range(M):
                if i&(1<<j):
                    temp.append(board[y][x+j])
            if sum(temp) <= C:
                realtemp = 0
                for i in temp:
                    realtemp += i*i
                if honey_temp < realtemp:
                    honey_temp = realtemp
        honey += honey_temp
        if flag: # B 꿀 계산
            # print(prevH, honey-prevH, y, x)
            if max_honey < honey:
                max_honey = honey
        else: # A 꿀 계산
            x += M
            for i, j in nextbee(y, x):
                myq.append((i, j, honey))
    print(f'#{tc}', max_honey)
