T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split())
    boxes = [0]*N
    for i in range(Q):
        L, R = map(int,input().split())
        boxes[L-1:R] = [i+1]*(R-L+1)
    print(f'#{tc}', *boxes)
