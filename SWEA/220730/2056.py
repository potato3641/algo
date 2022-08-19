T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    line = input()
    ly = line[:4]
    lm = line[4:6]
    ld = line[6:]
    print(f'#{test_case} ',end='')
    flag = False
    if int(lm) > 0 and int(lm) <= 12:
    	if int(ld) <= months[int(lm)-1] and int(ld) > 0:
            flag = True
    if flag:
        print(f'{ly}/{lm}/{ld}')
    else:
        print(f'-1')

