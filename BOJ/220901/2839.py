N = int(input())
a = N//5
if N%5==1:
    a += 1
elif N%5==2:
    a -= 2
    if a<0:
        a = -1
    else:        
        a += 4
elif N%5==3:
    a += 1
elif N%5==4:
    a -= 1
    if a<0:
        a = -1
    else:
        a += 3
print(a)
