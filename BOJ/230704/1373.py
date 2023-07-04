target = input()[::-1]
cnt = 1
answer = []
temp = 0
for i in target:
    temp += cnt*int(i)
    cnt *= 2
    if cnt == 8:
        cnt = 1
        answer.append(temp)
        temp = 0
else:
    if cnt > 1:
        answer.append(temp)
print(*answer[::-1],sep="")
