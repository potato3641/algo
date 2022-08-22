for tc in range(4):
    line = list(map(int,input().split()))
    # 첫직 x y p q 둘직 x y p q
    x1, y1, p1, q1 = line[:4]
    x2, y2, p2, q2 = line[4:]
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
    elif p1 == x2 or q1 == y2 or p2 == x1 or q2 == y1:
        case1 = p1==x2
        case2 = q1==y2
        case3 = p2==x1
        case4 = q2==y1
        if case1 + case2 + case3 + case4 > 1:
            print('c')
        else:
            print('b')
    else:
        print('a')
