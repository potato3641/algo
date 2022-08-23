T = 10
for tc in range(1, T+1):
    len_line = int(input())
    line = input()
    num_stack = []
    op_stack = []
    for i in line:
        if i.isdigit():   # 숫자니?
            num_stack.append(i) # 들어가
        else:
            if op_stack:
                if i == ')': # 괄호가 닫힐때 '('를 만날때까지 연산자 쏟아냄
                    while op_stack and op_stack[-1] != '(':
                        num_stack.append(op_stack.pop())
                    if op_stack: # 이제 '('는 나가
                        op_stack.pop()
                elif i == '+' and op_stack[-1] == '+': # 동일한 우선순위
                    num_stack.append(i)
                elif i == '*' and op_stack[-1] == '*': # 연산자면 그냥 들어가
                    num_stack.append(i)
                elif i == '+' and op_stack[-1] == '*': # 높은 우선순위가 스택에 있으면
                    num_stack.append(op_stack.pop())   # 그거 꺼내서 들어가게 하고
                    op_stack.append(i)                 # 니가 들어가
                else: # '(' 이거나, 스택에 '*'가 없는 '*'이거나, 스택에 '*'가 없는 '+'들
                    op_stack.append(i)
            else: # 스택이 비어있으면 그냥 넣어
                op_stack.append(i)
    else:
        while op_stack: # 잔여물 처리
            num_stack.append(op_stack.pop())
    back_str = ''.join(num_stack)
    stack = []
    for i in back_str: # 후위연산하는코드 풀었던거 그대~로 가져다가 붙임
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
    print(f'#{tc}', ''.join(num_stack))