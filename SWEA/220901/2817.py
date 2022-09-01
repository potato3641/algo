T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    line = list(map(int,input().split()))
    rst = 0
    for i in range(1<<N):
        temp = []
        for j in range(N):
            if i&(1<<j):
                temp.append(line[j])
        if sum(temp)==K:
            rst += 1
    print(f'#{test_case}', rst)
