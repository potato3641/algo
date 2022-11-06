def miis(): return map(int,input().split())
def ii(): return int(input())
debugger = False
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
M, S = miis()
temp = [list(miis()) for _ in range(M)] # y, x, d
fishinfo = []
for y, x, d in temp:
    fishinfo.append((y-1, x-1, d-1))
shark = tuple(miis()) # y, x
shark = tuple(x-1 for x in shark)
blooded = dict()
for _ in range(S):
# 복제(데이터 따로 빼두기)
    copyinfo = fishinfo[:]
# 이동
    fishinfo = dict()
    for y, x, d in copyinfo:
        cnt = 0
        while (y+dy[d], x+dx[d]) in blooded or (y+dy[d], x+dx[d]) == shark or not (0<=y+dy[d]<4 and 0<=x+dx[d]<4):
            d = (d-1)%8
            cnt += 1
            if cnt > 7:
                break
        if cnt == 8:
            if (y, x) in fishinfo:
                fishinfo[(y, x)].append(d)
            else:
                fishinfo[(y, x)] = [d]
            continue
        # if 0<=y+dy[d]<4 and 0<=x+dx[d]<4:
        if (y+dy[d], x+dx[d]) in fishinfo:
            fishinfo[(y+dy[d], x+dx[d])].append(d)
        else:
            fishinfo[(y+dy[d], x+dx[d])] = [d]
    if debugger: print(fishinfo)
# 상어 이동
    ddy = [-1, 0, 1, 0]
    ddx = [0, -1, 0, 1]
    sharked = {(shark[0], shark[1], 0, '', '')}
    for m in range(3):
        temp, sharked = set(sharked), set()
        for y, x, cnt, visit, order in temp:
            for d in range(4):
                if 0<=y+ddy[d]<4 and 0<=x+ddx[d]<4:
                    if (y+ddy[d], x+ddx[d]) in fishinfo:
                        if f'{hex((y+ddy[d])*4+x+ddx[d])[2:]}' not in visit:
                            sharked.add((y+ddy[d], x+ddx[d], cnt+len(fishinfo[(y+ddy[d], x+ddx[d])]), visit+f'{hex((y+ddy[d])*4+x+ddx[d])[2:]}', order+f'{d+1}'))
                        else:
                            sharked.add((y+ddy[d], x+ddx[d], cnt, visit+f'{hex((y+ddy[d])*4+x+ddx[d])[2:]}', order+f'{d+1}'))
                    else:
                        sharked.add((y+ddy[d], x+ddx[d], cnt, visit, order+f'{d+1}'))
    temp = sorted(list(sharked), key=lambda x: (-x[2], x[4]))
    if debugger: print('here is sort')
    if debugger: print(temp)
    y, x, cnt, visit, order = temp[0]
    shark = (y, x)
# 냄새 제거
    temp = list(blooded.keys())
    for i in temp:
        blooded[i] -= 1
        if blooded[i] <= 0:
            del blooded[i]
# 냄새 생성
    for v in visit:
        temp = int('0x'+v,16)
        if (temp//4, temp%4) in fishinfo:
            blooded[(temp//4, temp%4)] = 2
            del fishinfo[(temp//4, temp%4)]
    if debugger: print('here is visit')
    if debugger: print(visit)
    if debugger: print('here is blood')
    if debugger: print(blooded)
# 복제완료
    temp = []
    for i in fishinfo:
        for j in fishinfo[i]:
            temp.append((i[0], i[1], j))
    if debugger: print('here is fish')
    if debugger: print(fishinfo)
    if debugger: print('here is copy')
    if debugger: print(copyinfo)
    for y, x, d in copyinfo:
        temp.append((y, x, d))
    fishinfo = temp[:]
    if debugger: print('here is total')
    if debugger: print(fishinfo)
    if debugger:
        for i in range(4):
            for j in range(4):
                for d in range(8):
                    if (i, j, d) in fishinfo:
                        print('1', end=' ')
                        break
                else:
                    print('0', end=' ')
            print()
        print()
print(len(fishinfo))
