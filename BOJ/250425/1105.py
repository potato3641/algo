L, R = input().split()
cnt = 0
if len(L)==len(R):
    limit = len(L)
    idx = 0
    while idx < limit:
        if L[idx]==R[idx]:
            if L[idx]=="8":
                cnt += 1
        else:
            break
        idx += 1
print(cnt)
