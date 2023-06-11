N, m, M, T, R = map(int,input().split())
#현재 X
#운동 X+T (<=M)
#휴식 X-R (>=m)
cnt = 0
now = m
flag = False
while N:
    if now+T <= M:
        flag = False
        now += T
        N -= 1
    elif now-R >= m:
        flag = False
        now -= R
    else:
        if flag:
            cnt = -1
            break
        flag = True
        now = m
    cnt += 1
print(cnt)
