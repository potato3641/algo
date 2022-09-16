def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = int((N**(1/3)+0.5)//1)
    if N!=temp**3:
        temp = -1
    print(f'#{tc}', temp)
