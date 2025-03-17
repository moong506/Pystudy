n = int(input())
arr = [[1] * 10 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 10):
        arr[i][j] = (arr[i][j-1] + arr[i-1][j]) % 10007

print(arr[n][9])
