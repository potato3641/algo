T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = list(map(int,input().split()))
    basket = []
    enemy = 0
    for i in line:
        if i not in basket:
            basket.append(i)
        else:
            enemy = i
    if len(basket) > 1:
    	rst = int(basket[0]*basket[1]/enemy)
    else:
        rst = enemy
    print(f'#{test_case} {rst}')
