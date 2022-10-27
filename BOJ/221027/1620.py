import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
def miis(): return map(int,input().split())
def ii(): return int(input())
N, M = miis()
names = dict()
nums = dict()
for i in range(1, N+1):
    target = input()
    names[target] = i
    nums[i] = target
for _ in range(M):
    target = input()
    if target.isnumeric():
        print(nums[int(target)])
    else:
        print(names[target])
