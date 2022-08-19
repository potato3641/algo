T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    line = list(map(int,input().split()))
    last = line[-1]
    money = 0
    while True:
        max_num = max(line)
        idx = line.index(max_num)
        money += max_num*idx-sum(line[:idx])
        if line[idx] == last:
            break
        line = line[idx+1:]
    print(f'#{test_case} {money}')
