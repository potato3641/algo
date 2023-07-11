N = int(input())
val = 0
target = 44
while True:
    val += 1
    if N < target:
        break
    target *= 10
    target += 4
gmins = []
answer = 0
for i in range(1<<val):
    temp = []
    for j in range(val):
        if i&(1<<j):
            temp.append("4")
        else:
            temp.append("7")
    gmins.append(int(''.join(temp)))
gmins.sort()
for i in gmins:
    if i <= N:
        answer = i
    else:
        break
print(answer)
