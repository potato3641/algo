P, K = map(int,input().split())
carrier = [x for x in range(K,1,-1)]
odd = []
target = 0
while target < K**(1/2):
    target = carrier.pop()
    odd.append(target)
    carrier = [x for x in carrier if x%target!=0]
odd += carrier
working = False
for j in (x for x in odd if x <= P):
    if P%j == 0:
        working = True
        if j < K or P/j < K:
            print("BAD", j if j<P/j else int(P/j))
        else:
            print("GOOD")
        break
if not working:
    print("GOOD")