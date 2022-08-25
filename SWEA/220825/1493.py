def andpoint(val):
    i = 1
    while val > i*(i+1)//2:
        i += 1
    x_iter, y_iter = i*(i+1)//2-val, i*(i+1)//2-val
    return (i-x_iter, 1+y_iter)
def findval(tple):
    x, y = tple
    return x*(x+1)//2 + y*(y-1)//2 + (x-1)*(y-1)
    
T = int(input())
for tc in range(1, T+1):
    p, q = map(int,input().split())
    # 3, 3 - 13 = 1+2+3 + 3+4
    #             p       p부터 q-1개
    # 3, 4 = 1+2+3 + 3+4+5
    # 5, 2 = 1+2+3+4+5 5
    p = andpoint(p)
    q = andpoint(q)
    print(f'#{tc}', findval((p[0]+q[0],p[1]+q[1])))