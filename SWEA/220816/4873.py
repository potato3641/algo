T = int(input())
for tc in range(1, T+1):
    line = input()
    stack = []
    for i in line:
        if len(stack):
            if stack[-1] == i:
                stack.pop(-1)
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f'#{tc}', len(stack))
