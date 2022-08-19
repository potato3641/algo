T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    line = [1]
    print(f'#{test_case}')
    for i in range(N):
        a = [0]
        a.extend(line)
        b = line[:] + [0]
        line = [a[x]+b[x] for x in range(i+1)] if i else [1]
        print(*line)
