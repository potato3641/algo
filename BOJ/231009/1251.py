word = input()
maxval = len(word)
answers = []
for i in range(1, maxval-1):
    for j in range(i+1, maxval):
        answers.append(word[:i][::-1]+word[i:j][::-1]+word[j:][::-1])
answers.sort()
print(answers[0])
