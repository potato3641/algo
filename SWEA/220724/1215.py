T = 10
N = 8
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    F = int(input())
    board = []
    rst = 0
    for i in range(N):
        board.append(input())
    for i in range(N):
        for j in range(N-F+1):
            if board[i][j:j+F] == board[i][j:j+F][::-1]:
                #print(board[i][j:j+F], end=' ')
                rst += 1
    #print()
    for i in range(N-F+1):
        for j in range(N):
            colstr = ''.join([line[j] for line in board[i:i+F]])
            if colstr == colstr[::-1]:
                #print(colstr, end=' ')
                rst += 1
    print(f'#{test_case} {rst}')
