T = int(input())
for tc in range(1, T+1):
    line = input()
    stack = []
    rst = 1
    for i in line:
        if i == '{' or i == '(':
            stack.append(i)
        if i == '}':
            if len(stack):
                if stack.pop(-1) != '{':
                    rst = 0
            else:
                rst = 0
        if i == ')':
            if len(stack):
                if stack.pop(-1) != '(':
                    rst = 0
            else:
                rst = 0
    if len(stack):
        rst = 0
    print(f'#{tc}', rst)
