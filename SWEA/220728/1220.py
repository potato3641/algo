T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    basket = set()
    rst = 0
    for i in range(N):
        line = list(map(int,input().split()))
        for j in range(len(line)):
            if line[j] == 2 and j in basket:
                basket.discard(j)
                rst += 1
            elif line[j] == 1:
                basket.add(j)
    print(f'#{test_case} {rst}')
                
                
