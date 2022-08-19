alpha_set = set(list('abcdefghijklmnopqrstuvwxyz'))
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    word = []
    for i in range(N):
        word.append(input())
    rst = 0
    for i in range(1<<N):
        basket = []
        for j in range(N):
            if i&(1<<j):
                basket.append(word[j])
        if not len(alpha_set-set(list(''.join(basket)))):
            rst += 1
    print(f'#{test_case} {rst}') 
