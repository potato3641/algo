T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    line = [i+1 for i in range(12)]
    len_line = len(line)
    part_line = [[] for _ in range(1<<len_line)]
    for i in range(1<<len_line):
        for j in range(len_line):
            if i&(1<<j):
                part_line[i].append(line[j])
    rst = 0
    for i in part_line:
        if len(i) == N:
            part_sum = 0
            for j in i:
                part_sum += j
            if part_sum == K:
                rst += 1
    print(f'#{test_case} {rst}')
