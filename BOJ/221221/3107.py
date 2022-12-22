def miis(): return map(int,input().split())
def ii(): return int(input())
ipv6 = input().split(':')
if len(ipv6) > 8:
    if ipv6[0] == '':
        del ipv6[0]
    elif ipv6[-1] == '':
        del ipv6[-1]
ans = []
targetidx = -1
for i in range(len(ipv6)):
    if ipv6[i] == '':
        if targetidx == -1:
            targetidx = i
        ipv6[i] = '0000'
    ans.append('0'*(4-len(ipv6[i]))+ipv6[i]+':')

for i in range(8-len(ipv6)):
    ans.insert(targetidx,'0000:')
ans = ''.join(ans)
if ans[-1] == ':':
    print(ans[:-1])
else:
    print(ans)
