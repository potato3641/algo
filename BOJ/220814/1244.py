switch_N = int(input())
switch_line = [0] + list(map(int,input().split()))
student_N = int(input())
for _ in range(student_N):
    # 남 1 여 2
    gen, num = map(int,input().split())
    if gen-1: # 여
        cnt = 1
        switch_line[num] ^= 1
        while True:
            if num + cnt > switch_N or num - cnt < 1:
                break
            if switch_line[num+cnt] == switch_line[num-cnt]:
                switch_line[num+cnt] ^= 1
                switch_line[num-cnt] ^= 1
            else:
                break
            cnt += 1

    else: # 남
        for i in range(num,switch_N+1,num):
            switch_line[i] ^= 1
switch_line = switch_line[1:]
i = 0
while True:
    print_line = switch_line[i:i+20]
    print(*print_line)
    i += 20
    if i >= len(switch_line):
        break
