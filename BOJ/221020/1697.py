N, K = map(int,input().split())
if N >= K:
    print(N-K)
else:
    rst = K-N
    myq = {(N, 0)}
    visited = set()
    while myq:
        temp = set(myq)
        myq = set()
        for i, depth in temp:
            if i == K:
                rst = min(depth, rst)
                break
            if 0 <= i <= 100000 and i not in visited:
                visited.add(i)
                myq.add((i*2, depth+1))
                myq.add((i+1, depth+1))
                myq.add((i-1, depth+1))
    print(rst)
