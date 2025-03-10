N = int(input())
arr = list(map(int, input().split()))
stack = []

i = 0
result = 1

for i in range(N):

    if arr[i] == result:
        result += 1

        while stack and stack[-1] == result:
            stack.pop()
            result += 1
    else:
        stack.append(arr[i])

if not stack:
    print("Nice")
else:
    print("Sad")
