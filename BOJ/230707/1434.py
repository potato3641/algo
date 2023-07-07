N, M = map(int,input().split())
aline = list(map(int,input().split()))
bline = tuple(map(int,input().split()))
endline = len(aline)
for i in bline:
    idx = 0
    while idx < endline and aline[idx] < i:
        idx += 1
    if idx < endline:
        if aline[idx] >= i:
            aline[idx] -= i
print(sum(aline))
