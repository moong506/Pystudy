def solve(idx, arr):
    n = len(arr)
    if n == 1:
        result[-1].append(arr[0])
    else:
        middle = arr[n//2]
        result[idx].append(middle)
        left = arr[:n//2]
        right = arr[(n//2)+1:]
        solve(idx+1, left)
        solve(idx+1, right)

k = int(input())
arr = list(map(int, input().split()))
result = [[] for _ in range(k)]

solve(0, arr)
for ans in result:
    print(*ans)
