def gcd(a, b): # 최대공약수구하는 함수
    while b:
        temp = a%b
        a = b
        b = temp
    return a
def solution(arrayA, arrayB):
    if set(arrayA)&set(arrayB): # 중복 있으면 바로 0처리
        return 0
    cnt = 0
    leftA, rightA = 0, 0
    leftB, rightB = 0, 0
    for i in arrayA: # arrayA의 최대공약수
        if cnt:
            rightA = i
            if leftA > rightA:
                leftA = gcd(leftA,rightA)
            else:
                leftA = gcd(rightA, leftA)
        else:
            leftA = i
        cnt += 1
    cnt = 0
    for i in arrayB: # arrayB의 최대공약수
        if cnt:
            rightB = i
            if leftB > rightB:
                leftB = gcd(leftB,rightB)
            else:
                leftB = gcd(rightB, leftB)
        else:
            leftB = i
        cnt += 1
    for i in arrayB:
        if not i%leftA: # 나눠지면 해당 안 됨
            leftA = 0
            break
    for i in arrayA:
        if not i%leftB: # 나눠지면 해당 안 됨
            leftB = 0
            break
    return max(leftA, leftB) # 둘다 해당 안 되면 0, 해당 되면 그 중 큰 거
