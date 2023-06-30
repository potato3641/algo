N = input()
lenn = len(N)
answer = "NO"
if lenn > 1:
    for i in range(1, lenn):
        left, right = N[0:i], N[i:lenn]
        lval, rval = 1, 1
        for l in left:
            lval *= int(l)
        for r in right:
            rval *= int(r)
        if lval == rval:
            answer = "YES"
            break
print(answer)
