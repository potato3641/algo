N = int(input())
line = input()
answer = []
cnt = 0
temp = []
for i in range(len(line)):
    if N-cnt:
        cnt += 1
        temp.append(line[i])
    else:
        answer.append(temp)
        cnt = 1
        temp = [line[i]]
else:
    answer.append(temp)
for i in range(len(line)//N):
    if i%2:
        answer[i] = answer[i][::-1]
answer = tuple(map(tuple,zip(*answer)))
for i in answer:
    print(*i, sep="", end="")
print()
