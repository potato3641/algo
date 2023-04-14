T = int(input())
for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    if dist-int(dist) < 0.000001:
        dist = int(dist)
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif dist == 0:
        print(0)
    elif r1+r2 > dist:
        if (r2>r1 and dist+r1 == r2) or (r1>r2 and dist+r2 == r1):
            print(1)
        elif (r2>r1 and dist+r1 < r2) or (r1>r2 and dist+r2 < r1):
            print(0)
        else:
            print(2)
    elif r1+r2 < dist:
        print(0)
    elif r1+r2 == dist:
        print(1)
