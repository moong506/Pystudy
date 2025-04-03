string = input()
happy = 0
sad = 0
i = 0
while i < len(string)-2:
    if string[i] == ':' and string[i+1] == '-':
        if string[i+2] == ')':
            happy += 1
            i += 2
        elif string[i+2] == '(':
            sad += 1
            i += 2
        else:  # :- 이후 표정이 없는 경우
            i += 1
    i += 1

if happy == sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:  # 두 표정의 개수가 0이 아니고 똑같이 나온 경우
    print('unsure')