import sys
sys.stdin = open('input.txt')
N, L = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
visited = []
for i in range(N):
    prevH, prevV = 0, 0
    breakH, breakV = True, True
    usedH, usedV = -1, -1
    cntH, cntV = 0, 0
    fstH, fstV = True, True
    # 값이 커질때 여유공간 확인하고 부족하면 false
    # 값이 작아질땐 처음만 여유공간 확인 안하고 다음엔 똑같이 false
    
    for j in range(N):
        if breakH:
            if prevH == 0: # 처음이니
                cntH = 1
            elif prevH == board[i][j]: # 평지니
                cntH += 1
            elif abs(prevH-board[i][j])>1: # 경사가 너무 높니
                breakH = False
            elif prevH < board[i][j]: # 값이 커지니
                if fstH:
                    fstH = False
                if cntH < L: # 자리 부족하니
                    breakH = False
                else: # 설치자리 여유롭니
                    if usedH+L >= j: # 뭐가 설치되어있니
                    # if j-1 <= usedH: 
                        breakH = False
                    cntH = 1
                    usedH = j-1
                    # print('H', i, usedH)
            elif prevH > board[i][j]: # 값이 작아지니
                if fstH:
                    fstH = False
                    if j+L-1 >= N:
                        breakH = False
                    usedH = j+L-1
                    # print('H', i, usedH)
                else:
                    if cntH < L: # 자리 부족하니
                        breakH = False
                    else: # 설치 자리 여유롭니
                        cntH = 1
                        if j <= usedH:
                            breakH = False
                        usedH = j+L-1
                        # print('H', i, usedH)
            prevH = board[i][j]
        if breakV:
            if prevV == 0: # 처음이니
                cntV = 1
            elif prevV == board[j][i]: # 평지니
                cntV += 1
            elif abs(prevV-board[j][i])>1: # 경사가 너무 높니
                breakV = False
            elif prevV < board[j][i]: # 값이 커지니
                if fstV:
                    fstV = False
                if cntV < L: # 자리 부족하니
                    breakV = False
                else: # 설치자리 여유롭니
                    if usedV+L >= j: # 뭐가 설치되어있니
                    # if j-1 <= usedV:
                        breakV = False
                    cntV = 1
                    usedV = j-1
                    # print('V', i, usedV)
            elif prevV > board[j][i]: # 값이 작아지니
                if fstV:
                    fstV = False
                    if j+L-1 >= N:
                        breakV = False
                    usedV = j+L-1
                    # print('V', i, usedV)
                else:
                    if cntV < L: # 자리 부족하니
                        breakV = False
                    else: # 설치 자리 여유롭니
                        cntV = 1
                        if j <= usedV:
                            breakV = False
                        usedV = j+L-1
                        # print('V', i, usedV)
            prevV = board[j][i]
    if breakH:
        visited.append(('H', i))
    if breakV:
        visited.append(('V', i))
    ans += breakH+breakV
# print(visited)
print(ans)
