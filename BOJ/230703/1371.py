alphadict = dict()
for i in 'abcdefghijklmnopqrstuvwxyz ':
    alphadict[i] = 0
while True:
    try:
        for i in input():
            alphadict[i] += 1
    except:
        break
del alphadict[" "]
val = max(alphadict.values())
answer = []
for i in alphadict:
    if alphadict[i] == val:
        answer.append(i)
print(*answer, sep="")
