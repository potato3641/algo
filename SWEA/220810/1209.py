T = 10
for test_case in range(1, T + 1):
    input()
    list_2dim = []
    max_val = 0
    for i in range(100):
        line = list(map(int,input().split()))
        sum_line = 0
        for j in line:
            sum_line += j
        if max_val < sum_line:
            max_val = sum_line
        list_2dim.append(line)
    for i in range(100):
        sum_ver_line = 0
        sum_cross_line = 0
        sum_cross_line += list_2dim[i][i]
        sum_revcross_line = 0
        sum_revcross_line += list_2dim[i][99-i]
        for j in range(100):
            sum_ver_line += list_2dim[j][i]
        if max_val < sum_ver_line:
            max_val = sum_ver_line
    if max_val < sum_cross_line:
        max_val = sum_cross_line
    if max_val < sum_revcross_line:
        max_val = sum_revcross_line
    print(f'#{test_case} {max_val}')
        
