N, K = map(int,input().split())
temp = list(map(int,input().split()))
hap = sum(temp[:K])
max_hap = sum(temp[:K])
for i in range(K, N):
    hap += temp[i] - temp[i-K]
    if max_hap < hap:
        max_hap = hap
print(max_hap)
