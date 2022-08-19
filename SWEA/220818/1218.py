T = 10
for tc in range(1, T+1):
    N = int(input())
    line = input()
    level = {'(': 0, '{': 0, '[': 0, '<': 0}
    rst = 1
    for i in line:
        if i == '(' or i == '{' or i == '[' or i == '<':
            level[i] += 1
        elif i == ')':
            level['('] -= 1
        elif i == '}':
            level['{'] -= 1
        elif i == ']':
            level['['] -= 1
        elif i == '>':
            level['<'] -= 1
        for j in level:
            if level[j] < 0:
                rst = 0
    for j in level:
        if level[j]:
            rst = 0
    print(f'#{tc}', rst)
