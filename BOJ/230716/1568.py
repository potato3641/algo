N = int(input())
target = 1
cnt = 0
while N:
    if target <= N:
        N -= target
        target += 1
        cnt += 1
    else:
        target = 1
print(cnt)
