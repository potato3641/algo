data = []
while True:
    try:
        line = input()
    except EOFError:
        break
    data.append(line)
for line in data:
    alx, aly, arx, ary, blx, bly, brx, bry = map(float,line.split())
    if (alx, aly) == (blx, bly): # 1 3
        print("{:.3f} {:.3f}".format(brx+arx-alx,bry+ary-aly))
    elif (alx, aly) == (brx, bry): # 1 4
        print("{:.3f} {:.3f}".format(blx+arx-alx, bly+ary-aly))
    elif (arx, ary) == (blx, bly): # 2 3
        print("{:.3f} {:.3f}".format(brx+alx-arx, bry+aly-ary))
    else: # 2 4
        print("{:.3f} {:.3f}".format(blx+alx-arx, bly+aly-ary))