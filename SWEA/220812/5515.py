T = int(input())
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    M, D = map(int,input().split())
    print(f'#{test_case}', (3 + sum(months[:M-1])+D)%7)
