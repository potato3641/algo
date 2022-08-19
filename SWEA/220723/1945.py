T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    stat = [2,3,5,7,11]
    line = [0 for _ in range(5)]
    print(f'#{test_case}',end=' ')
    for i in range(len(stat)):
    	while True:
            if N%stat[i] == 0:
                N //= stat[i]
                line[i] += 1
            else:
                print(f'{line[i]}',end=' ')
                break
    print()
