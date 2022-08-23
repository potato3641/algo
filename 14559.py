import sys
sys.stdin = open('input.txt')
def gcd(a, b):
    while b:
        temp = a%b
        a = b
        b = temp
    return a
def lcm(a, b):
    return a*b//gcd(a, b)
def dfs(s, e):
    for i in range(s):
        
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