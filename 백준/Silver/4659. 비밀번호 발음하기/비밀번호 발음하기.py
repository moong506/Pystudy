while True:

    string = input()
    if string == 'end':
        break
    mo = ['a', 'e', 'i', 'o', 'u']
    mo_flag = False
    mo_count = 0
    ja_count = 0
    mo_ja_flag = True
    count_flag = True
    for i in range(len(string)):
        if string[i] in mo:
            mo_flag = True
            mo_count += 1
            ja_count = 0
        else:
            mo_count = 0
            ja_count += 1
        if mo_count >= 3 or ja_count >= 3:
            mo_ja_flag = False
            break
    

    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            if string[i] == 'e' or string[i] == 'o':
                pass
            else:
                count_flag = False
                break
        
    if mo_flag and mo_ja_flag and count_flag:
        print(f'<{string}> is acceptable.')
    else:
        print(f'<{string}> is not acceptable.')
