def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(miis()) for _ in range(N)]
    min_taste = -1
    setfood = []
    for i in range(1<<N):
        temp = set()
        for j in range(N):
            if i&(1<<j):
                temp.add(j)
        if len(temp) == N//2:
            setfood.append(temp)
    for i in setfood:
        btaste = 0
        j = [x for x in range(N) if x not in i]
        for b_mat1 in j:
            for b_mat2 in j:
                if b_mat1 != b_mat2:
                    btaste += board[b_mat1][b_mat2]
        ataste = 0
        for a_mat1 in i:
            for a_mat2 in i:
                if a_mat1 != a_mat2:
                    ataste += board[a_mat1][a_mat2]
        # print(i, btaste, btaste-ataste, ataste)
        taste = abs(btaste-ataste)
        if min_taste == -1 or min_taste > taste:
            min_taste = taste
    print(f'#{tc}', min_taste)
    # break
