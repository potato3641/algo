T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    amond = input()
    lines = ['' for _ in range(5)]
    lines[0] += '.'
    lines[1] += '.'
    lines[2] += '#'
    lines[3] += '.'
    lines[4] += '.'
    for i in range(5):
        for j in range(len(amond)):
            if i%2 == 1:
                lines[i] += '#.#.'
            else:
                if i == 2:
                    lines[i] += '.'+amond[j]+'.#'
                else:
                	lines[i] += '.#..'
        print(lines[i])
    
