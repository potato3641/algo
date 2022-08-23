import sys
sys.stdin = open('input.txt')
def gcd(a, b):
    while b:
        temp = a%b
        a = b
        b = temp
    return a
def lcm(a, b): # 최소공배수
    return a*b//gcd(a, b)
<<<<<<< HEAD
def dfs(s, e):
    for i in range(s):
        
=======
def dfs(SARR, EARR, SVAL, EVAL):
    # idea : 공배수 집합 판별
    temp = []
    for s in SARR:

>>>>>>> 6cb9d0807d1de800b5efcd18bc13392d2ff9b30b
RST = 0
T = int(input())
for tc in range(1, T+1):
    N, S, E = map(int,input().split())
    M = int(input())
    A, B = [], []
    RST = 0
    for _ in range(M):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
<<<<<<< HEAD
    start_idx, end_idx = [], []
    for a in range(A):
        if S%A[a] == 0:
            start_idx.append(a)
    for b in B:
        if E%B[b] == 0:
            end_idx.append(b)
    if start_idx + end_idx == False:
        print(f'-1')
    dfs(A, B)
=======
    dfs(A, B, S, E)
>>>>>>> 6cb9d0807d1de800b5efcd18bc13392d2ff9b30b
