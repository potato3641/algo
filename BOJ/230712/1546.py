N = int(input())
line = list(map(int,input().split()))
target = max(line)
for i in range(N):
    line[i] = line[i]/target*100
print(sum(line)/N)
