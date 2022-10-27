import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
S = 0
for _ in range(N):
    line = input()
    if line == 'all':
        S = 1048575
    elif line == 'empty':
        S = 0
    else:
        order, num = line.split()
        num = int(num)-1
        if order == 'add':
            if S&(1<<num):
                continue
            S += 1<<num
        elif order == 'remove':
            if S&(1<<num):
                S -= 1<<num
        elif order == 'check':
            if S&(1<<num):
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            S ^= 1<<num
