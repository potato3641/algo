T = int(input())
for test_case in range(1, T + 1):
    line = input()
    if len(set(line)) == 2 and line.count(set(line).pop())==2:
        print(f'#{test_case} Yes')
        continue
    print(f'#{test_case} No')
