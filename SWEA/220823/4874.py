T = int(input())
for tc in range(1, T+1):
    line = input().split()
    stack = []
    for i in line:
        if i.isdigit():
            stack.append(int(i))
        else:
            if len(stack) < 2 and i != '.':
                break
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x - y)
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                y = stack.pop()
                x = stack.pop()
                if y:
                    stack.append(x//y)
                else:
                    break
    else:
        if len(stack) == 1:
            print(f'#{tc}', stack.pop())
            continue
    print(f'#{tc} error')