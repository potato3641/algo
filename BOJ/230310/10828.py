T = int(input())
stack = []
siz = 0
resultStack = []
for tc in range(T):
    order = input()
    if "push" in order:
        line = order.split()
        if len(stack) == siz:
            stack.append(int(line[1]))
        else:
            stack[siz] = int(line[1])
        siz += 1
    elif "pop" in order:
        if siz:
            resultStack.append(stack[siz-1])
            siz -= 1
        else:
            resultStack.append(-1)
    elif "size" in order:
        resultStack.append(siz)
    elif "empty" in order:
        if siz:
            resultStack.append(0)
        else:
            resultStack.append(1)
    elif "top" in order:
        if siz:
            resultStack.append(stack[siz-1])
        else:
            resultStack.append(-1)
print("\n".join(map(str,resultStack)))
