T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    tot = 0
    for i in range(N):
        line = input()
        for j in range(N):
            if (N//2-i if i-N//2 < 0 else i-N//2) + (N//2-j if j-N//2 < 0 else j-N//2) <= N//2:
                tot += int(line[j])
    print(f'#{test_case} {tot}')
                
