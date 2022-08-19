T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = list(map(int,input().split()))
    mint = (line[0] + line[2])*60 + (line[1] + line[3])
    print(f'#{test_case} {12 if mint//60%12 == 0 else mint//60%12} {mint%60}')
