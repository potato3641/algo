for _ in range(int(input())):
    temp = input()
    L = 10**len(temp)
    N = int(temp)
    print("YES" if N*N%L==N else "NO")
