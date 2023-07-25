line = input()
pwd = input()
lenpwd = len(pwd)
crypto = dict()
target = "abcdefghijklmnopqrstuvwxyz"
cnt = 1
for i in target:
    crypto[i] = cnt
    cnt += 1
answer = []
idx = 0
for i in line:
    if i == " ":
        answer.append(" ")
    else:
        answer.append(target[(crypto[i]-crypto[pwd[idx]]-1)%26])
    idx += 1
    idx %= lenpwd
print(*answer, sep="")

