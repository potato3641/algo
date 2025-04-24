N = int(input())
carrier = [x for x in range(1000000,1,-1)]
odd = []
target = 0
while target < 1000000**(1/2):
    target = carrier.pop()
    odd.append(target)
    carrier = [x for x in carrier if x%target!=0]
odd = carrier + odd
for i in range(N):
    num = int(input())
    flag = True
    for j in odd:
        if num%j == 0:
            flag = False
            break
    print("YES" if flag else "NO")