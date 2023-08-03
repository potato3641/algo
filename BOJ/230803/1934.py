def getgcd(a, b):
    while b:
        temp = a%b
        a = b
        b = temp
    return a
for _ in range(int(input())):
    a, b = map(int,input().split())
    print(a*b//getgcd(a, b))
