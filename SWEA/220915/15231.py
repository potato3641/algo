T = int(input())
mydict = dict()
lognums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912]
for i in range(len(lognums)):
    mydict[lognums[i]] = i
ans = ['']*T
for tc in range(1, T+1):
    N, V = map(int,input().split())
    tempN = N
    tempV = V
    while tempN&(tempN-1):
        tempN = tempN&(tempN-1)
    while tempV&(tempV-1):
        tempV = tempV&(tempV-1)
    rst = mydict[tempN]+mydict[tempV]
    if N < (tempN+tempN*2)//2 and V < (tempV+tempV*2)//2:
        rst -= 1
    if tc==1:
        ans[tc-1] =  f'#{tc} {rst}'
    else:
        ans[tc-1] =  f'\n#{tc} {rst}'
print(*ans)

