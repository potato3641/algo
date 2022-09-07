T = int(input())
for test_case in range(1, T + 1):
    line = int(input())
    for i in range(2, 10):
        if sorted(list(str(line))) == sorted(list(str(line*i))):
            print(f'#{test_case} possible')
            break
    else:
        print(f'#{test_case} impossible')
