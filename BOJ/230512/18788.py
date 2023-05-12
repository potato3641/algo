N, M = map(int,input().split())
orders = list(tuple(map(int,input().split())) for _ in range(2))
line = tuple(x for x in range(1, N+1))
origin_line = line[:]
visited = [tuple(line)]
cnt = 0
while True:
    for start, end in orders:
        line = line[:start-1] + line[start-1:end][::-1] + line[end:]
    cnt += 1
    if line != origin_line:
        visited.append(line)
    else:
        break
M %= cnt
for i in visited[M]:
    print(i)
