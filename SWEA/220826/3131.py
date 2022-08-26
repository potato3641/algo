carrier = [x for x in range(1000000,1,-1)]
ans = []
target = 0
while target < 1000000**(1/2):
    target = carrier.pop()
    ans.append(target)
    carrier = [x for x in carrier if x%target!=0]
print(*ans, end=' ')
print(*carrier[::-1])