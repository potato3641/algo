A, B = input().split()
A = A[::-1]
B = B[::-1]
answer = []
minlen = min(len(A), len(B))
maxlen = max(len(A), len(B))
amp = 0
for i in range(minlen):
    temp = int(A[i]) + int(B[i]) + amp
    amp = 0
    if temp > 1:
        amp = 1
        temp %= 2
    answer.append(temp)
target = A if len(A)==maxlen else B
for i in range(minlen, maxlen):
    temp = int(target[i]) + amp
    amp = 0
    if temp > 1:
        amp = 1
        temp %= 2
    answer.append(temp)
if amp:
    answer.append(1)
while answer and not answer[-1]:
    answer.pop()
if not answer:
    answer.append(0)
print(*answer[::-1],sep='')
