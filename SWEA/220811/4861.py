T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    basket = []
    rst = ''
    for i in range(N):
        basket.append(input())
    for i in range(N):
        versket = [x[i] for x in basket]
        for j in range(N-M+1):
            if basket[i][j:j+M] == basket[i][j:j+M][::-1]:
                rst = basket[i][j:j+M]
            if versket[j:j+M] == versket[j:j+M][::-1]:
                rst = ''.join(versket[j:j+M])
    print(f'#{test_case} {rst}')
