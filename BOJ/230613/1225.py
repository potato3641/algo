A, B = map(tuple,input().split())
answer = 0
mem = dict()
for i in map(int,A):
    if i in mem:
        answer += mem[i]
    else:
        temp = 0
        for j in map(int,B):
            temp += i*j
        mem[i] = temp
        answer += mem[i]
print(answer)
