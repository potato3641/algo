T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    kN = 0
    sheepSET = set()
    while len(sheepSET) < 10:
        kN += N 
        strN = str(kN)
        for i in range(len(strN)):
            sheepSET.add(int(strN[i]))
    print(f'#{test_case} {kN}')
