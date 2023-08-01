N = int(input())
goodp = "nice"
badp = "not nice"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(N):
    temp, right = input().split("-")
    right = int(right)
    amp = 1
    left = 0
    for i in temp[::-1]:
        left += amp*alpha.index(i)
        amp *= 26
    if abs(left-right) <= 100:
        print(goodp)
    else:
        print(badp)
