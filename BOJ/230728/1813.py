N = int(input())
line = tuple(map(int,input().split()))
answer = set()
for i in range(1, 51):
    if i == line.count(i):
        answer.add(i)
else:
    if answer:
        print(max(answer))
    else:
        if 0 in line:
            print(-1)
        else:
            print(0)
