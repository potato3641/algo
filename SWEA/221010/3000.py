import heapq
def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    N, S = miis()
    mins = []
    maxs = []
    mid = S
    rst = 0
    for i in range(N):
        X, Y = miis()
        if X > mid:
            heapq.heappush(mins, X)
        else:
            heapq.heappush(maxs, (-X, X))
        if len(maxs) > len(mins)+1:
            heapq.heappush(mins, mid)
            mid = heapq.heappop(maxs)[1]
        elif len(maxs)+1 < len(mins):
            heapq.heappush(maxs, (-mid, mid))
            mid = heapq.heappop(mins)
        if Y > mid:
            heapq.heappush(mins, Y)
        else:
            heapq.heappush(maxs, (-Y, Y))
        if len(maxs) > len(mins)+1:
            heapq.heappush(mins, mid)
            mid = heapq.heappop(maxs)[1]
        elif len(maxs)+1 < len(mins):
            heapq.heappush(maxs, (-mid, mid))
            mid = heapq.heappop(mins)
        rst += mid%20171109
    print(f'#{tc}', rst%20171109)



