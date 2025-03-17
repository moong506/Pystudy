def backtracking(n, m, length, arr):
    if length == m:
        print(*arr)
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                arr[length] = i+1
                length += 1
                visited[i] = 1
                backtracking(n, m, length, arr)
                length -= 1
                visited[i] = 0


n, m = map(int, input().split())
visited = [0] * n
arr = [0] * m
length = 0
backtracking(n, m, length, arr)
