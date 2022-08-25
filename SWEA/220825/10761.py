import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, *line = input().split()
    flag = ''
    rst = 0
    B_cur = 1
    O_cur = 1
    for i in range(N):
        flag = line[i*2]
        rst += line[i*2+1]

    print(f'#{tc}')