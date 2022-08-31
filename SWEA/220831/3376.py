T = int(input())
for test_case in range(1, T + 1):
    memo = dict()
    for i in range(1,101):
        if i<=3:
            memo[i] = 1
        elif i<=5:
            memo[i] = 2
        else:
            memo[i] = memo[i-1]+memo[i-5]
    print(f'#{test_case}', memo[int(input())])
    
