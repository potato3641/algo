T = int(input())
for i in range(T):
    input()
    N, M = map(int,input().split())
    aline = tuple(map(int,input().split()))
    bline = tuple(map(int,input().split()))
    if max(aline) < max(bline):
        print("B")
        continue
    elif max(aline) > max(bline):
        print("S")
        continue
    else:
        target = max(max(aline), max(bline))
        acnt = aline.count(target)
        bcnt = bline.count(target)
        if acnt < bcnt:
            print("B")
        else:
            print("S")
