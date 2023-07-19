N = int(input())
line = [int(input()) for _ in range(N)]
for a in range(2):
    target = line[::-1] if a else line
    top = 0
    cnt = 0
    for i in target:
        if top < i:
            top = i
            cnt += 1
    print(cnt)
