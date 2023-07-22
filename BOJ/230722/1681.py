N, L = input().split()
N = int(N)
num = 1
while N:
    if L not in str(num):
        N -= 1
    num += 1
print(num-1)
