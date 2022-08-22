get_char = input()
len_char = 0
for i in ['dz=','c=','c-','d-','lj','nj','s=','z=']:
    while get_char.find(i) != -1:
        get_char = get_char[:get_char.find(i)] + ' ' + get_char[get_char.find(i)+len(i):]
len_char += len(get_char)
print(len_char)
