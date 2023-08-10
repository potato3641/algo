N = int(input())
prevcnt = 1
cnt = 10
upper = (5, 6, 7, 8, 9)
while N//cnt:
    target = N%cnt
    if N%cnt//prevcnt in upper:
        N += cnt-target
    else:
        N -= target 
    cnt *= 10
    prevcnt *= 10
print(N)
