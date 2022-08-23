T = int(input())
for tc in range(1, T+1):
    cnt = 0
    prev = '.'
    for i in input():
        if i == '|' and prev == '(':
            cnt += 1
        if i == ')' and prev == '|':
            cnt += 1
        if i == ')' and prev == '(':
            cnt += 1
        prev = i
    print(f'#{tc}', cnt)