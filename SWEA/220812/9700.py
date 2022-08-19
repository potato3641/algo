T = int(input())
for tc in range(1, T + 1):
    p, q = map(float,input().split())
    if q*(1-p)<p*(1-q)*q:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
