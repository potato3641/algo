origin = int(input())
N = origin+0
cnt = 0
while True:
    N = N%10*10+(N%10+N//10)%10
    cnt += 1
    if N == origin:
        break
print(cnt)
