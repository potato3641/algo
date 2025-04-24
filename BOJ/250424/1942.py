def clockInt(h, m, s):
    return int(h+m+s)
for _ in range(3):
    S, E = input().split()
    clockE = ""
    for x in E.split(":"):
        clockE += x
    clockE = int(clockE)
    ans = 1 if clockE%3==0 else 0
    h, m, s = S.split(":")
    while clockInt(h,m,s) != clockE:
        ans = ans+1 if clockInt(h,m,s)%3==0 else ans
        s = "{0:02d}".format(int(s)+1)
        if int(s) > 59:
            m = "{0:02d}".format(int(m)+1)
            if int(m) > 59:
                h = "{0:02d}".format(int(h)+1)
                if int(h) > 23:
                    h = "00"
                m = "00"
            s = "00"
    print(ans)

