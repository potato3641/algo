T = int(input())
for tc in range(1, T+1):
    line = input()
    laser_flag = False
    new_line = ''
    for i in line:
        if i == '(':
            laser_flag = True
            new_line += i
        if i == ')':
            if laser_flag:
                laser_flag = False
                new_line = new_line[:-1] + 'L'
            else:
                new_line += i
    stick_stack = 0
    static_stack = 0
    rst = 0
    for i in new_line:
        if i == '(':
            stick_stack += 1
        elif i == ')':
            stick_stack -= 1
            static_stack += 1
        else:
            if static_stack:
                rst += static_stack
                static_stack = 0
            rst += stick_stack
    else:
        rst += static_stack
    print(f'#{tc} {rst}')
