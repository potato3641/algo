line = tuple("0123456789ABCDEF")
answer = 0
amp = 1
target = input()
for i in target[::-1]:
    answer += line.index(i)*amp
    amp *= 16
print(answer)
