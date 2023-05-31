N = int(input())
line = list(input() for _ in range(N))
answer = []
for i in range(len(line[0])):
    temp = set()
    for j in range(N):
        temp.add(line[j][i])
    if len(temp) > 1:
        answer.append('?')
    else:
        answer.append(temp.pop())
print(''.join(answer))
