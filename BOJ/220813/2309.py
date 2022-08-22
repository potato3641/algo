line = []
for i in range(9):
    line.append(int(input()))
sum_line = sum(line)
for i in range(9):
    kid1 = line[i]
    new_line = line[:i] + line[i+1:]
    for j in new_line:
        if sum_line - kid1 - j == 100:
            line.remove(line[i])
            line.remove(j)
            line.sort()
            break
    if len(line) == 7:
        for i in line:
            print(i)
        break
