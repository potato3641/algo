T = 10
for tc in range(1, T+1):
    N = int(input())
    line = input()
    num_stack = []
    op_stack = []
    for i in line:
        if 48 <= ord(i) < 58:
            num_stack.append(i)
        else:
            if i == '+':
                if op_stack:
                    while op_stack:
                        num_stack.append(op_stack.pop())
                op_stack.append(i)
            else:
                op_stack.append(i)
    else:
        if op_stack:
            while op_stack:
                num_stack.append(op_stack.pop())
    stack = []
    for i in num_stack:
        if 48 <= ord(i) < 58:
            stack.append(i)
        else:
            if i == '+':
                stack.append(int(stack.pop(-1))+int(stack.pop(-1)))
            else:
                stack.append(int(stack.pop(-1))*int(stack.pop(-1)))
    print(f'#{tc}', stack.pop())
