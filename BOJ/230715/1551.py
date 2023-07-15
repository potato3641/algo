N, K = map(int,input().split())
line = list(map(int,input().split(",")))
while K:
    answer = []
    for i in range(1, N):
        answer.append(line[i]-line[i-1])
    line = answer
    N -= 1
    K -= 1
print(*line,sep=",")
