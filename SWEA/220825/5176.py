T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [0]*(N+1)
    # 레벨은 2**(n-1)부터 2**n-1까지 n레벨
    # n레벨 1
    # n-1레벨 2
    level = 0
    val = N
    while val:
        val //= 2
        level += 1
    level -= 1
    one_idx = 2**level
    val = 1
    idx = one_idx
    cnt_leaf = 0
    while True:
        board[idx] = val
        val += 2
        idx += 1
        cnt_leaf += 1
        if idx > N:
            break
    val = 2
    idx = one_idx//2
    while not board[idx]:
        board[idx] = val
        val += 2
        idx += 1
        if idx*2 <= N and board[idx*2]:
            val += 1
        if idx*2-1 <= N and board[idx*2-1]:
            val += 1
    print(f'#{tc}', one_idx - (0 if cnt_leaf >= one_idx//2 else (one_idx//2)-cnt_leaf), board[N//2])
    # board[cnt] = 1
    # board[cnt//2] = 2 # 내 부모
    # board[cnt+1] = 3 # 내 오른쪽 친구
    # 어쩄든 맨 밑줄과 그 윗줄 채워놓고
    # 그 정보들을 통해서 루트와 N/2를 구하는거    