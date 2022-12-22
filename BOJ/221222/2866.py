def miis(): return map(int,input().split())
def ii(): return int(input())
N, M = miis()
board = [tuple(input()) for _ in range(N)]
myq = [(1, N)]
ans = 0
while myq:
    S, E = myq.pop()
    if S > E:
        break
    m = (S+E)//2
    strset = set()
    flag = True
    for i in range(M):
        temp = ''
        for j in range(m, N):
            temp += board[j][i]
        if temp in strset:
            flag = False
            break
        else:
            strset.add(temp)
    if flag:
        if ans < m:
            ans = m
        myq.append((m+1, E))
    else:
        myq.append((S, m-1))
print(ans)
