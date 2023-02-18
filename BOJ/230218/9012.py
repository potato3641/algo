T = int(input())
for tc in range(1, T+1):
    line = input()
    level = 0
    for s in line:
        if s == "(":
            level += 1
        else:
            level -= 1
        if level < 0:
            break
    if level > 0 or level < 0:
        print("NO")
    else:
        print("YES")
