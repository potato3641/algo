def log2(n):
    cnt = 0
    while n//2:
        n >>= 1
        cnt += 1
    return cnt
mydict = dict()
T = int(input())
ans = ''
for tc in range(1, T+1):
    N, V = map(int,input().split())
    level = -1
    my_level = -1
    if N in mydict:
        level = mydict[N]
    else:
        level = log2(N)
        mydict[N] = level
    if V in mydict:
        my_level = mydict[V]
    else:
        my_level = log2(V)
        mydict[V] = my_level
    rst = level + my_level
    if N < (2**level+2**(level+1))//2 and V < (2**my_level+2**(my_level+1))//2:
        rst -= 1
    ans += f'#{tc} ' + str(rst) + '\n'
    if tc >= 50000:
        break
print(ans)
