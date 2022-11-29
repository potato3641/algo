def ii(): return int(input())

N = ii()
lastdance = {'ChongChong'}
for _ in range(N):
    A, B = input().split()
    if A in lastdance:
        lastdance.add(B)
    elif B in lastdance:
        lastdance.add(A)
print(len(lastdance))
