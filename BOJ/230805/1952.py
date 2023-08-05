M, N = map(int,input().split())
mydict = dict()
def fibo(a, b):
    if (a, b) in mydict:
        return mydict[(a, b)]
    elif a==1:
        return 0
    elif b==1:
        return 1
    elif a==2:
        return 2
    elif b==2:
        return 3
    mydict[(a,b)] = fibo(a-2,b-2)+4
    return mydict[(a,b)]
print(fibo(M, N))
