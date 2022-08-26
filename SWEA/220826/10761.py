T = int(input())
for tc in range(1, T+1):
    N, *line = input().split()
    N = int(N)
    B = []
    O = []
    # B B O
    # B와 O 이동은 별개
    # O O
    # O만 이동 열심히
    # B O O B
    # B B O O로 봐도되니까 두개 분리해
    for i in range(N):
        if line[i*2] == 'B':
            B.append((i+1, int(line[i*2+1])))
        if line[i*2] == 'O':
            O.append((i+1, int(line[i*2+1])))
    b_cur, o_cur = 0, 0
    b_pos, o_pos = 1, 1
    timer = 0
    i = 1
    while True:
        timer += 1 
        flag = True
        # print('now :', timer, '/ B :', b_pos, '/ O :', o_pos)
        if b_cur < len(B) and b_pos < B[b_cur][1]:
            b_pos += 1
        elif b_cur < len(B) and b_pos > B[b_cur][1]:
            b_pos -= 1
        elif b_cur < len(B):
            if flag and i == B[b_cur][0]:
                b_cur += 1
                i += 1
                flag = False
        if o_cur < len(O) and o_pos < O[o_cur][1]:
            o_pos += 1
        elif o_cur < len(O) and o_pos > O[o_cur][1]:
            o_pos -= 1
        elif o_cur < len(O):
            if flag and i == O[o_cur][0]:
                o_cur += 1
                i += 1
                flag = False
        if b_cur >= len(B) and o_cur >= len(O):
            break
    print(f'#{tc}', timer)
