for _ in range(3):
    line = sum(int(input()) for _ in range(int(input())))
    print(("+" if line>0 else "-") if line else 0)
