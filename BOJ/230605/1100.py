cnt = 0
for _ in range(4):
    temp = list(input())
    for i in (0,2,4,6):
        if temp[i] == 'F':
            cnt += 1
    temp = list(input())
    for i in (0,2,4,6):
    for i in (1,3,5,7):
        if temp[i] == 'F':
            cnt += 1
print(cnt)
