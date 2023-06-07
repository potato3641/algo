line = tuple(map(int,input().split()))
def gcd(a, b):
    while b:
        temp = a%b
        a = b
        b = temp
    return a
minans = float('inf')
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ij = line[i]*line[j]//gcd(line[i], line[j])
            ijk = ij*line[k]//gcd(ij, line[k])
            if minans > ijk:
                minans = ijk
print(minans)
