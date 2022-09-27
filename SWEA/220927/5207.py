def miis(): return map(int,input().split())
def bsearch(target, b, l, r):
    global searchcnt
    if l<=r:
        m = (l+r)//2
        if A[m]==target:
            searchcnt += 1
        else:
            if b == 0:
                bsearch(target, -1, l, m-1)
                bsearch(target, 1, m+1, r)
            elif b == 1:
                bsearch(target, -1, l, m-1)
            elif b == -1:
                bsearch(target, 1, m+1, r)
searchcnt = 0
T = int(input())
for tc in range(1, T+1):
    N, M = miis()
    A = sorted(list(miis()))
    B = list(miis())
    searchcnt = 0
    for i in B:
        bsearch(i, 0, 0, N-1)
    print(f'#{tc}', searchcnt)
