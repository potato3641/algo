T = int(input())
same = {0, 1, 5, 6}
pattern = dict()
pattern[2] = (2, 4, 8, 6)
pattern[3] = (3, 9, 7, 1)
pattern[4] = (4, 6)
pattern[7] = (7, 9, 3, 1)
pattern[8] = (8, 4, 2, 6)
pattern[9] = (9, 1)
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a in same:
        if a:
            print(a)
        else:
            print(10)
    else:
        b -= 1
        b %= len(pattern[a])
        print(pattern[a][b])
