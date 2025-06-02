N = int(input())
arr = list(map(int, input().split()))
ans = [0]*N
stack = [0]*N
top = 0

for i in range(N):
    while top >= 0:
        if arr[stack[top]] <= arr[i]:
            top -= 1
        elif arr[stack[top]] > arr[i]:
            ans[i] = stack[top] + 1
            top += 1
            stack[top] = i
            break
    else:
        top = 0
        stack[top] = i




print(*ans)