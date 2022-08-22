get_char = input()
sensored_char = ''
for i in get_char:
    if i not in 'CAMBRIDGE':
        sensored_char += i
print(sensored_char)
