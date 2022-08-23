T = int(input())
for tc in range(1, T+1):
    line = input()
    if line.count('o') >= 8 or line.count('x') < 8:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')