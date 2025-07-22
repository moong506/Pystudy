import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = [0] * N
top = -1
i = 0
for target in range(1, N):
    if top >=0 and stack[top] == target:
        top -= 1
        continue
    while i < N:
        if arr[i] == target:
            i += 1
            break
        else:
            top += 1
            stack[top] = arr[i]
            i += 1
    else:
        print('Sad')
        break
else:
    print('Nice')