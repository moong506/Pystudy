arr = input()
upper_str = arr.upper()
str_dict ={}
for word in upper_str:
    if word in str_dict.keys():
        str_dict[word] += 1
    else:
        str_dict[word] = 1
max_value = 0
max_key = '?'
flag = False
for key, value in str_dict.items():
    if max_value < value:
        flag = False
        max_value = value
        max_key = key
    elif max_value == value:
        flag = True
if flag:
    print('?')
else:
    print(max_key)
