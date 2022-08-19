T = int(input())
for tc in range(1, T + 1):
    line = input()[::-1]
    new_line = ''
    for i in line:
        if i == 'p':
            new_line += 'q'
        elif i == 'q':
            new_line += 'p'
        elif i == 'b':
            new_line += 'd'
        else:
            new_line += 'b'
    print(f'#{tc} {new_line}')
