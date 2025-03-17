N = int(input())
stack = [0] * 10000
top = -1

for _ in range(N):
    a, *b = input().split() # push x, pop, size, empty, top
    
    if a == 'push': # 스택에 넣기
        top += 1
        stack[top] = b[0]

    elif a == 'pop': # 스택에서 꺼내기
        if top >= 0:
            print(stack[top])
            top -= 1
        else: # 스택이 비었다면 -1 출력
            print(-1)

    elif a == 'size': # 스택 크기 출력
        print(top+1)

    elif a == 'empty': # 스택이 비어있으면 1, 아니면 0
        if top == -1:
            print(1)
        else:
            print(0)

    elif a == 'top': # 스택 가장 위 출력, 스택이 비었다면 -1
        if top >= 0:
            print(stack[top])
        else:
            print(-1)