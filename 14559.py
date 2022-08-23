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
def dfs(SARR, EARR, SVAL, EVAL):
    # idea : 공배수 집합 판별
    temp = []
    for s in SARR:

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
    dfs(A, B, S, E)
