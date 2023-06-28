N = int(input())
line = tuple(map(int,input().split()))
csize = int(input())
answer = 0
for i in line:
    if i:
        if i <= csize:
            answer += 1
        else:
            answer += i//csize+(1 if i%csize else 0)
print(answer*csize)
