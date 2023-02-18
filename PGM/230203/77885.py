def solution(numbers):
    answer = []
    for i in numbers:
        if i%2==0:
            answer.append(i+1)
        else:
            cnt = 0
            temp = i>>1
            while temp%2:
                temp = temp>>1
                cnt += 1
            answer.append(i+pow(2,cnt))
    return answer
