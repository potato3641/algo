def ii(): return int(input())

N = ii()
print(sum(int(input().split('-')[1])<=90 for _ in range(N)))


