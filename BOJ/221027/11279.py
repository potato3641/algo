import sys, os, io, atexit, heapq
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
arr = []
for _ in range(N):
    order = ii()
    if order:
        heapq.heappush(arr, -order)
    else:
        if len(arr):
            print(-heapq.heappop(arr))
        else:
            print(0)

