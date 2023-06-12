convert = dict()
bins = '000001010011100101110111'
for i in range(8):
    convert[str(i)] = bins[i*3:(i+1)*3]
answer = []
first = True
for i in input():
    answer.append(convert[i])
while answer[0] and answer[0][0] == '0':
    answer[0] = answer[0][1:]
if len(answer) == 1 and not len(answer[0]):
    print(0)
else:
    print(*answer,sep='')
