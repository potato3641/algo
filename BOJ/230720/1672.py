N = int(input())
target = input()
if N == 1:
    print(target)
else:
    mydict = dict()
    tables = "ACAGCGTAATCGGAGT"
    idx = 0
    for i in "AGCT":
        for j in "AGCT":
            mydict[i+j] = tables[idx]
            idx += 1
    bases = target[-1]
    for i in target[-2::-1]:
        bases = mydict[bases+i]
    print(bases)
