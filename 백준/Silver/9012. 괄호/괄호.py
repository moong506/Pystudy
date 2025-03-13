T = int(input())

for tc in range(1, T+1):
    words = input() # 괄호 문자열 받기
    ans = 'YES' # 초기화
    stack = []

    for w in words: # 괄호 문자열 앞부터 보면서
        if w == '(': # 여는 괄호면 스택에 넣기
            stack.append(w)
        elif w == ')': # 닿는 괄호면
            if stack: # 스택이 차있는 동안
                while True: # ( 만날때까지 꺼내기
                    next = stack.pop()
                    if next == '(':
                        break;
            else: # 더 꺼낼 수 없다면 짝이 안맞는 것! NO로 바꾸고 break
                ans = 'NO'
                break;

    # 다 꺼냈는데 스택에 뭔가 남아있다면 NO로 바꿈
    if stack:
        ans = 'NO'

    print(ans)