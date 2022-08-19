def swap_line(line):
    swap_line = []
    for j in range(99):
        if line[j+1] == (line[j] + 1) and line[j] > 0:
            swap_line.append(line[j])
        else:
            if len(swap_line) > 0:
                swap_line.append(line[j])
                swap_line[1:-1] = [0]*(len(swap_line)-2)
                swap_line = swap_line[::-1]
                line[line.index(swap_line[-1]):j+1] = swap_line[:]
                swap_line = []
    if len(swap_line) > 0:
        swap_line.append(line[j+1])
        swap_line[1:-1] = [0]*(len(swap_line)-2)
        swap_line = swap_line[::-1]
        line[line.index(swap_line[-1]):j+2] = swap_line[:]
        swap_line = []
    return line
T = 10
for test_case in range(1, T + 1):
    input()
    ladder_book = []
    start_idx = 0
    for i in range(100):
        temp = list(map(int,input().split()))
        if i == 99:
            start_idx = [x+1 for x in range(100) if temp[x]==1]
        idx_temp = [x+1 if temp[x] > 0 else 0 for x in range(100)]
        idx_temp = swap_line(idx_temp)
        ladder_book.append(idx_temp)
    min_dist = 10000
    min_start = 0
    for j in start_idx:
        dist = 0
        for i in range(100):
            j = ladder_book[99-i][j-1]
            dist += abs(ladder_book[99-i][j-1] - j)
        if min_dist > dist:
            min_dist = dist
            min_start = j
    print(f'#{test_case}', min_start-1)
