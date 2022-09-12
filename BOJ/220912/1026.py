N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())),reverse=True)
rst = 0
for i in range(N):
    rst += A[i]*B[i]
print(rst)
