T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    line = input().split()
    suffle_line = [0]*N
    cent_idx = (N+1)//2
    suffle_flag = True
    cnt = 0
    for i in range(N):
        if suffle_flag:
            suffle_flag = False
            suffle_line[i] = line[cnt]
        else:
            suffle_flag = True
            suffle_line[i] = line[cnt+cent_idx]
            cnt += 1
    print(f'#{test_case}', *suffle_line)
