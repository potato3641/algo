M = int(input())
N = int(input())
S = int(M**0.5)
E = int(N**0.5)+1
answer = []
for i in range(S, E):
    if M <= i*i <= N:
        answer.append(i*i)
if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
