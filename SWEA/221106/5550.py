def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    croak = input()
    len_croak = len(croak)
    if len_croak%5:
        print(f'#{tc} -1')
        continue
    frogcnt = 0
    max_frogcnt = 0
    cc, rr, oo, aa, kk = 0, 0, 0, 0, 0
    for i in croak:
        if i == 'c':
            cc += 1
            frogcnt += 1
            if max_frogcnt < frogcnt:
                max_frogcnt = frogcnt
        elif i == 'r':
            rr += 1
        elif i == 'o':
            oo += 1
        elif i == 'a':
            aa += 1
        elif i == 'k':
            kk += 1
            frogcnt -= 1
        if not (cc>=rr>=oo>=aa>=kk):
            max_frogcnt = -1
            break
    if not(cc==rr==oo==aa==kk):
        max_frogcnt = -1
    print(f'#{tc}', max_frogcnt)
