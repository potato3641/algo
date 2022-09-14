import math
N, K, M = map(int,input().split())
def demens(n, d):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, d)
        rev_base = str(mod)+' '+rev_base
    return rev_base
N_M = list(map(int,demens(N, M).split()))
K_M = list(map(int,demens(K, M).split()))
if len(N_M) > len(K_M):
    K_M = [0]*(len(N_M)-len(K_M)) + K_M
rst = 1
for i in range(len(N_M)):
    if N_M[i] < K_M[i]:
        rst = 0
        break
    else:
        rst *= (math.factorial(N_M[i])//math.factorial(N_M[i]-K_M[i]))//math.factorial(K_M[i])
print(rst%M)
