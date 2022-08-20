T = int(input())
for test_case in range(1, T + 1):
    cnt_card = int(input())
    cards = int(input())
    basket = [0]*10
    while cnt_card:
        basket[cards % 10] += 1
        cnt_card -= 1
        if cards:
            cards = cards//10
    max_num = 0
    max_cnt = 0
    for i in range(10):
        if basket[i] > max_cnt:
            max_num = i
            max_cnt = basket[i]
        elif basket[i] == max_cnt and i > max_num:
            max_num = i
            max_cnt = basket[i]
    print(f'#{test_case} {max_num} {max_cnt}')
