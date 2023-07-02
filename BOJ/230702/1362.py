num = 0
while True:
    num += 1
    o, w = map(int,input().split())
    if o == w == 0:
        break
    ripflag = False
    while True:
        a, b = input().split()
        if a == "#":
            break
        elif a == "F":
            w += int(b)
        elif a == "E":
            w -= int(b)
            if w <= 0:
                ripflag = True
    if ripflag:
        print(num, "RIP")
    elif o//2 < w < o*2:
        print(num, ":-)")
    else:
        print(num, ":-(")
