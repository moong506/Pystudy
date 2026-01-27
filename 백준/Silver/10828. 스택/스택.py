N = int(input())
top = 0
arr = [0]*N
for i in range(N):
    command, *num = input().split()
    if command == 'push':
        arr[top] = num[0]
        top += 1
    elif command == 'pop':
        if top == 0:
            print(-1)
        else:
            top -= 1
            print(arr[top])
    elif command == 'size':
        print(top)
    elif command == 'empty':
        if top == 0:
            print(1)
        else:
            print(0)
    else:  # command == 'top'
        if top == 0:
            print(-1)
        else:
            print(arr[top-1])
