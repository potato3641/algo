td = dict()
td[1] = 1
td[2] = 2
td[3] = 3
for _ in range(int(input())):
    X, Y = map(int,input().split())
    td[X], td[Y] = td[Y], td[X]
for i in td:
    if td[i]==1:
        print(i)
        break
else:
    print(-1)
