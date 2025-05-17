N = int(input())
arr = list(map(int, input().split()))
arr.sort()
used = [0] * N

for i in range(N):
    goal = arr[i]
    start = 0
    end = N - 1
    while start < end:
        if arr[start] + arr[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                used[i] = 1
                break

        elif arr[start] + arr[end] > goal:
            end -= 1
        else:
            start += 1
count = 0
for i in range(N):
    if used[i] == 1:
        count += 1

print(count)