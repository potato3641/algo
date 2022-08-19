T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M1, D1, M2, D2 = map(int,input().split())
    marr = [31,28,31,30,31,30,31,31,30,31,30,31]
    M1 -= 1
    M2 -= 1
    rst = sum(marr[:M2])-sum(marr[:M1])+D2-D1+1
    print(f'#{test_case} {rst}')
