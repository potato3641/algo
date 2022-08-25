import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    line = list(map(int,input().split()))
    vals = set()
    for i in line:
        for j in line:
            if j != i:
                for k in line:
                    if k != i and k != j:
                        vals.add(i+j+k)
    for _ in range(4):
        vals.remove(max(vals))
    print(f'#{tc}', max(vals))