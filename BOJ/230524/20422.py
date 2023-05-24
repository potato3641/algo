name = list(input())
origin =   list('AEHIMOSTUVWXYZbdilmnopqruvwx0123578')
symmetry = list('A3HIMO2TUVWXY5dbilmnoqp7uvwx01SEZr8')
solo = list('AHIMOTUVWXYilmnouvwx018')
small_alpha = 'abcdefghijklmnopqrstuvwxyz'
big_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = small_alpha+big_alpha
mirror = []
for i in range(len(name)):
    if name[i] in origin:
        continue
    elif name[i].upper() in origin:
        name[i] = name[i].upper()
    elif name[i].lower() in origin:
        name[i] = name[i].lower()
for i in name:
    if i in origin:
        mirror.append(symmetry[origin.index(i)])
mirror = ''.join(mirror)
originame = ''.join(name[:])
for idx in range(len(mirror)+1):
    name = originame + mirror[:idx][::-1]
    lename = len(name)
    available = True
    answerleft = ''
    answerright = ''
    for i in range((len(name)+1)//2):
        left = name[i]
        right = name[lename-i-1]
        qdr_left = []
        qdr_right = []
        qdr_left.append(left)
        if left in alphabet:
            if left in small_alpha:
                qdr_left.append(left.upper())
            elif left in big_alpha:
                qdr_left.append(left.lower())
        qdr_right.append(right)
        if right in alphabet:
            if right in small_alpha:
                qdr_right.append(right.upper())
            elif right in big_alpha:
                qdr_right.append(right.lower())
        worked = False
        for j in range(len(qdr_left)):
            target = qdr_left[j]
            if target in origin:
                symtarget = symmetry[origin.index(target)]
                for k in range(len(qdr_right)):
                    if qdr_right[k] == symtarget:
                        worked = True
                        answerleft += target
                        if i != lename-1-i:
                            answerright = symtarget + answerright
                        break
            if worked:
                break
        if not worked:
            available = False
            break
    if available:
        print(answerleft + answerright)
        break
if not available:
    print(-1)
