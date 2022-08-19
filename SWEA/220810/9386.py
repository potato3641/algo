T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    line = input()
    cur_num = 0
    max_num = 0
    for i in line:
        if i == '1':
            cur_num +=1
            if max_num < cur_num:
                max_num = cur_num
        else:
            cur_num = 0
    print(f'#{test_case} {max_num}')
