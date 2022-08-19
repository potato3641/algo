T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    pj = []
    target = 0
    for i in range(N):
        line = list(map(int,input().split()))
        pj.append(line[0]*0.35 + line[1]*0.45 + line[2]*0.2)
        if i+1 == K:
            target = pj[i]
    pjs = sorted(pj)
    for i in range(len(pjs)):
        if pjs[i] == target:
            if i < N/10:
            	print(f'#{test_case} D0')
            elif i < N/10*2:
                print(f'#{test_case} C-')
            elif i < N/10*3:
                print(f'#{test_case} C0')
            elif i < N/10*4:
                print(f'#{test_case} C+')
            elif i < N/10*5:
                print(f'#{test_case} B-')
            elif i < N/10*6:
                print(f'#{test_case} B0')
            elif i < N/10*7:
                print(f'#{test_case} B+')
            elif i < N/10*8:
                print(f'#{test_case} A-')
            elif i < N/10*9:
                print(f'#{test_case} A0')
            else:
                print(f'#{test_case} A+')
            break
