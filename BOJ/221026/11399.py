N=int(input())
line=list(map(int,input().split()))
line.sort(reverse=True)
ans=0
for i in range(1,N+1):
    ans += line[i-1]*i
print(ans)

# 숏코딩 86B
# input()
# print(sum(v*i for i,v in enumerate(sorted(map(int,input().split()))[::-1],1)))