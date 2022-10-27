import sys, os, io, atexit
from heapq import heappop, heappush
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
def miis(): return map(int,input().split())
def ii(): return int(input())

T = ii()
for tc in range(1, T+1):
    N = ii()
    deleted = dict()
    minheap = []
    maxheap = []
    now_cap = 0
    for _ in range(N):
        order, num = input().split()
        num = int(num)
        if order == 'I':
            now_cap += 1
            heappush(minheap, num)
            heappush(maxheap, -num)
            if num in deleted:
                deleted[num] += 1
            else:
                deleted[num] = 1
        else:
            if now_cap:
                now_cap -= 1
                if num == 1:
                    while deleted[-maxheap[0]] < 1:
                        heappop(maxheap)
                    if maxheap:
                        deleted[-heappop(maxheap)] -= 1
                else:
                    while deleted[minheap[0]] < 1:
                        heappop(minheap)
                    if minheap:
                        deleted[heappop(minheap)] -= 1
    if now_cap:
        while deleted[-maxheap[0]] < 1:
            heappop(maxheap)
        while deleted[minheap[0]] < 1:
            heappop(minheap)
        print(-heappop(maxheap), heappop(minheap))
    else:
        print('EMPTY')
