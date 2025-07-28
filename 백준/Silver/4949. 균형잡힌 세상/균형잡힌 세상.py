
while True:
    string = input()
    if string == '.':
        break
    stack = [0]*len(string)
    top = -1
    for word in string:
        if word =='.':
            if top >= 0:
                print('no')
            else:
                print('yes')
            break
        elif word == '(':
            top += 1
            stack[top] = '('
        elif word == '[':
            top += 1
            stack[top] = '['
        elif word == ')':
            if top < 0 or stack[top] != '(':
                print('no')
                break
            else:
                top -= 1
        elif word == ']':
            if top < 0 or stack[top] != '[':
                print('no')
                break
            else:
                top -= 1
