def hcheck(n):
    return n in range(1, 13)
def mscheck(n):
    return n in range(60)
line = tuple(map(int,input().split(":")))
cnt = 0
for i in range(3):
    for j in range(3):
        if i != j:
            for k in range(3):
                if i != k and j != k:
                    if hcheck(line[i]) and mscheck(line[j]) and mscheck(line[k]):
                        cnt += 1
print(cnt)
