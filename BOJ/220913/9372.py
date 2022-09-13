import sys
input = sys.stdin.readline
T = int(input())
ans = ''
for _ in range(T):
    N, M = map(int,input().split())
    for _ in range(M):
        input()
    ans += str(N-1) + '\n'
print(ans, end='')
