N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N-1, -1, -1):
#     if arr[i][0] + i <= 7
max_result = 0
def recur(x, y):
    global max_result
    if y == N:
        max_result = max(max_result, x)
        return
    if y > N:
        return
    recur(x + arr[y][1], y + arr[y][0])
    recur(x, y + 1)
recur(0, 0)
print(max_result)
