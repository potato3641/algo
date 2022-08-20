T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    line = list(map(int,input().split()))
    basket, min_idx, max_idx = [0]*101, 1, 0
    new_line = [0]*10
    for i in line:
        basket[i] += 1
    for i in range(101):
        while basket[i] > 0 and min_idx < 10:
            basket[i] -= 1
            new_line[min_idx] = i
            min_idx += 2
        while basket[100-i] > 0 and max_idx < 10:
            basket[100-i] -= 1
            new_line[max_idx] = 100-i
            max_idx += 2
    print(f'#{test_case} ', end='')
    print(*new_line[:10])
