N = int(input())
line = tuple(map(int,input().split()))
Y = 0
M = 0
for i in line:
    Y += 10*(i//30+1)
    M += 15*(i//60+1)
if Y<M:
    print("Y", Y)
elif M<Y:
    print("M", M)
else:
    print("Y M", Y)
