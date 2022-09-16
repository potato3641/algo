alphaset = 'abcdefghijklmnopqrstuvwxyz'
T = int(input())
for tc in range(1, T+1):
    wrd = input()
    K = int(input())
    banwrd = set()
    for i in alphaset:
        if wrd.count(i) < K:
            banwrd.add(i)
    wrdarray = []
    for i in range(len(wrd)):
        if wrd[i] in banwrd:
            continue
        cnt = 0
        wrdlen = 0
        for _ in range(K):
            finder = wrd[i+wrdlen:].find(wrd[i])
            if finder != -1:
                wrdlen += finder+1
                cnt += 1
            else:
                break
        if cnt == K:
            # print(i, wrd[i], wrdlen)
            wrdarray.append(wrdlen)
    if len(wrdarray):
        print(min(wrdarray), max(wrdarray))
    else:
        print(-1)
