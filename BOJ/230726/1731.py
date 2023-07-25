N = int(input())
line = tuple(int(input()) for _ in range(N))
a, b, c = line[-3], line[-2], line[-1]
if b-a == c-b:
    print(c+c-b)
else:
    print(c*(c//b))
