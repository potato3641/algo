def miis(): return map(int,input().split())
def clockorder(roach, dir):
    if dir == 1:
        return [roach[-1]] + roach[:-1]
    else:
        return roach[1:] + [roach[0]]
    
toproach = [list(input()) for _ in range(4)]
N = int(input())
orders = [list(miis()) for _ in range(N)]
# 1. 평형 확인
# 2. order 받고
# 3. 돌리기
for i in range(N):
    target, direc = orders[i]
    target -= 1
    # 2는 오른쪽 6은 왼쪽
    line = []
    for i in range(4):
        line.append((toproach[i][2], toproach[i][6]))
    cnt = 1
    rotated = [target]
    righton = True
    lefton = True
    while lefton or righton:
        if righton and target+cnt<4: # 오른쪽톱
            if line[target+cnt][1] != line[target+cnt-1][0]: # 극이 같니
                rotated.append(target+cnt)
            else:
                righton = False
        else:
            righton = False
        if lefton and target-cnt>=0: # 왼쪽톱
            if line[target-cnt][0] != line[target-cnt+1][1]: # 극이 같니
                rotated.append(target-cnt)
            else:
                lefton = False
        else:
            lefton = False
        cnt += 1
    for i in rotated:
        toproach[i] = clockorder(toproach[i], direc*(-1 if (target-i)%2 else 1))
        # print(i, direc*(-1 if (target-i)%2 else 1))
ans = 0
for i in range(4):
    if toproach[i][0] == '1':
        ans += 1<<i
print(ans)
