def miis(): return map(int,input().split())
def ii(): return int(input())
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1 ,-1]
N, M, K = miis()
fireballinfo = [tuple(miis()) for _ in range(M)]
for _ in range(K):
    # 이동
    mydict = dict()
    for r, c, m, s, d in fireballinfo:
        y, x = (r+dy[d]*s)%N, (c+dx[d]*s)%N
        if (y, x) in mydict:
            mydict[(y, x)].append((m, s, d))
        else:
            mydict[(y, x)] = [(m, s, d)]
    # 합체
    # 분열
    # 소멸
    fireballinfo = []
    for i in mydict:
        if len(mydict[i]) > 1:
            adderM = sum(x[0] for x in mydict[i])//5
            if adderM == 0:
                continue
            adderS = sum(x[1] for x in mydict[i])//len(mydict[i])
            dirline = []
            if sum(x[2]%2 for x in mydict[i]) in [0, len(mydict[i])]: # 0 2 4 6
                dirline = [0,2,4,6]
            else: # 1 3 5 7
                dirline = [1,3,5,7]
            for d in dirline:
                fireballinfo.append((i[0], i[1], adderM, adderS, d))
        else:
            fireballinfo.append((i[0], i[1], mydict[i][0][0], mydict[i][0][1], mydict[i][0][2]))
print(sum(x[2] for x in fireballinfo))
