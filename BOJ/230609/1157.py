def upalpha(n): return n.upper()
N = tuple(map(upalpha,input()))
cnt = sorted(list((x, N.count(x)) for x in set(N)), key=lambda x: -x[1])
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print("?")
else:
    print(cnt[0][0])
