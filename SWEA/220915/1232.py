T = 10
for tc in range(1, T+1):
    N = int(input())
    ininfo = [list(input().split()) for _ in range(N)]
    board = [[] for _ in range(N+1)]
    opboard = [[] for _ in range(N+1)]
    for i in range(N):
        target = int(ininfo[i][0])
        opboard[target] = ininfo[i][1]
        if len(ininfo[i]) > 2:
            board[target].append(int(ininfo[i][2]))
            board[target].append(int(ininfo[i][3]))
    myq = []
    myq.append(1)
    opq = []
    while True:
        # pop
        if len(myq): # 꺼내기 단계
            target = myq.pop()
            if len(board[target]): # 연산자 노드라면
                opq.append(opboard[target])
                myq.append(board[target][0])
                myq.append(board[target][1])
            else:
                opq.append(opboard[target])
                while len(opq) > 2 and not opq[-3].isdigit( ) and opq[-2].lstrip('-').isdigit( ) and opq[-1].lstrip('-').isdigit( ): # 연산자와 그 밑이 완성되었다면
                    leftnum = int(opq.pop())
                    rightnum = int(opq.pop())
                    operand = opq.pop()
                    if operand == '+':
                        opq.append(str(leftnum + rightnum))
                    elif operand == '-':
                        opq.append(str(leftnum - rightnum))
                    elif operand == '*':
                        opq.append(str(leftnum * rightnum))
                    elif operand == '/':
                        opq.append(str(leftnum // rightnum))
        else:
            if len(opq) > 1:
                while len(opq) > 2 and not opq[-3].isdigit( ) and opq[-2].lstrip('-').isdigit( ) and opq[-1].lstrip('-').isdigit( ): # 연산자와 그 밑이 완성되었다면
                    leftnum = int(opq.pop())
                    rightnum = int(opq.pop())
                    operand = opq.pop()
                    if operand == '+':
                        opq.append(str(leftnum + rightnum))
                    elif operand == '-':
                        opq.append(str(leftnum - rightnum))
                    elif operand == '*':
                        opq.append(str(leftnum * rightnum))
                    elif operand == '/':
                        opq.append(str(leftnum // rightnum))
            else:
                break
    print(f'#{tc}', int(opq[0]))
