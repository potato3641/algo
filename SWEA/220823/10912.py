T = int(input())
for tc in range(1, T+1):
    rst = ''
    prev = 0
    line = sorted(list(input()))
    for i in range(1, len(line)):
        if line[prev] == line[i]:
            line[prev:i+1] = ['', '']
        prev = i
    if ''.join(line) == '':
        print(f'#{tc} Good')
    else:
        print(f'#{tc}', ''.join(line))