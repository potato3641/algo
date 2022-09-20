def cvt(n, pow=1):
    zcnt = 0
    ocnt = 0
    brey = []
    for i in n[::-1]:
        if int(i):
            if zcnt:
                brey.append(zcnt)
                zcnt = 0
            ocnt += 1
        else:
            if ocnt:
                brey.append(ocnt)
                ocnt = 0
            zcnt += 1
    else:
        if ocnt:
            brey.append(ocnt)
        if zcnt:
            brey.append(zcnt)
    rst = 0
    for i in brey[::-1]:
        rst *= 10
        rst += i//pow
    return rst
pw = list(map(int,'3211 2221 2122 1411 1132 1231 1114 1312 1213 3112'.split()))
hexvar = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    real_line = []
    line = [list(input().strip()) for _ in range(N)]
    memo = []
    caseval = 0
    for i in range(N):
        if line[i].count('0') == M:
            continue
        codes = line[i][:]
        codes = ''.join(codes)
        hexcodes = ''
        # convert hex 2 pw
        for j in range(len(codes)):
            hexcodes += hexvar[int(codes[j],16)]
        fatalflag = True
        while fatalflag:
            if hexcodes.count('0') == len(hexcodes):
                break
            targetidx = len(hexcodes)-hexcodes[::-1].index('1')
            hexcodes = hexcodes[:targetidx]
            samplecnt = 7
            while cvt(hexcodes[-samplecnt:], samplecnt//7) not in pw:
                samplecnt += 7
            if not fatalflag or hexcodes[-samplecnt*8:] in memo:
                hexcodes = hexcodes[:-samplecnt*8]
                continue
            else:
                memo.append(hexcodes[-samplecnt*8:])
            rst = 0
            ans = 0
            for j in range(8):
                if j == 0:
                    ans += pw.index(cvt(hexcodes[-samplecnt*j-samplecnt:], samplecnt//7))
                    rst += pw.index(cvt(hexcodes[-samplecnt*j-samplecnt:], samplecnt//7))
                else:
                    ans += pw.index(cvt(hexcodes[-samplecnt*j-samplecnt:-samplecnt*j], samplecnt//7))
                    if j%2:
                        rst += pw.index(cvt(hexcodes[-samplecnt*j-samplecnt:-samplecnt*j], samplecnt//7))*3
                    else:
                        rst += pw.index(cvt(hexcodes[-samplecnt*j-samplecnt:-samplecnt*j], samplecnt//7))
            if not rst%10:
                caseval += ans
            hexcodes = hexcodes[:-samplecnt*8]
    print(f'#{tc}', caseval)
