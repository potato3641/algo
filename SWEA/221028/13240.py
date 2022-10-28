def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    N, M, Q = miis()
    if Q:
        line = list(map(len,input().split()))
    else:
        print(f'#{tc}', 0)
        continue
    if N==0 or M==0 or max(line) > M:
        print(f'#{tc}', 0)
        continue
		# 공간이 없거나 글자가 공간 초과하면 얄짤없음
    fontsize = 1
    while True:
        linecnt = 0
        heightcnt = 1
        isfirst = True
        for i in line:
            if isfirst: # 첫 번째 줄의 특권
                if i*fontsize > M: # 이면서 검사해야함
                    heightcnt = float('inf')
                    break
                else:
                    linecnt = i # 첫 번째 줄은 그냥 넣음
            else:
                if (1+linecnt+i)*fontsize > M:
                    if i*fontsize > M: # 이거 안넣어서 17개
                        heightcnt = float('inf')
                        break
                    linecnt = i
                    heightcnt += 1
                else:
                    linecnt += 1+i # 두 번째줄 부터 공백포함해서 넣기
            isfirst = False
        #     print(linecnt, heightcnt)
        # print(heightcnt, i, linecnt, fontsize)
        if heightcnt*fontsize > N:
            print(f'#{tc}', fontsize-1)
            break
        fontsize += 1
