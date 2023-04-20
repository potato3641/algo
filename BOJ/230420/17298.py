N = int(input())
line = list(map(int,input().split()))[::-1]
box = []
stack = []
for i in line:
    while stack and stack[-1] < i:
        stack.pop()
    if not stack:
        stack.append(i)
    if stack[-1] > i:
        box.append(stack[-1])
        stack.append(i)
    elif stack[-1] == i:
        if len(stack) == 1:
            box.append(-1)
        else:
            box.append(stack[-2])
print(*box[::-1])
