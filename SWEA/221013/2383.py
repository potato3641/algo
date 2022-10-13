def miis(): return map(int,input().split())
def ii(): return int(input())
def sims(n):
    ua, ub = 0, 0
    for i in range(len(tempA)):
        if tempA[i] > 0:
            tempA[i] -= 1
        elif tempA[i] == 0:
            if ua < 3:
                ua += 1
                tempA[i] -= 1
        elif tempA[i] + Afit >= 0:
            ua += 1
            tempA[i] -= 1
            if tempA[i] + Afit < 0:
                ua -= 1
    for i in range(len(tempB)):
        if tempB[i] > 0:
            tempB[i] -= 1
        elif tempB[i] == 0:
            if ub < 3:
                ub += 1
                tempB[i] -= 1
        elif tempB[i] + Bfit >= 0:
            ub += 1
            tempB[i] -= 1
            if tempB[i] + Bfit < 0:
                ub -= 1
    if tempA.count(-Afit-1) == len(tempA) and tempB.count(-Bfit-1) == len(tempB):
        return n
    return sims(n+1)
T = ii()
for tc in range(1, T+1):
    N = ii()
    board = [list(miis()) for _ in range(N)]
    people = []
    floors = dict()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] > 1:
                floors[(i, j)] = board[i][j]
    P = len(people)
    min_val = float('inf')
    for i in range(1<<P):
        tempA = []
        tempB = []
        floorA = list(floors.keys())[0]
        floorB = list(floors.keys())[1]
        for j in range(P):
            if i&(1<<j):
                tempA.append(abs(people[j][0]-floorA[0])+abs(people[j][1]-floorA[1]))
            else:
                tempB.append(abs(people[j][0]-floorB[0])+abs(people[j][1]-floorB[1]))
        tempA.sort()
        tempB.sort()
        Afit = floors[floorA]
        Bfit = floors[floorB]
        now_val = sims(1)
        if min_val > now_val:
            min_val = now_val
    print(f'#{tc}', min_val)
