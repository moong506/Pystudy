import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [list(map(int, input().split())) for _ in range(n)]


d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited = [[0] * m for _ in range(n)]
    isShark = 0  # flag
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= X < m and 0 <= Y < n and visited[Y][X] == 0:
                if arr[Y][X] == 0:
                    q.append((Y, X))
                    visited[Y][X] = visited[y][x] + 1
                else:
                    ans = visited[y][x] + 1
                    isShark = 1
        if isShark:
            break

    return ans


ans = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] != 1:
            if ans < bfs(y, x):
                ans = bfs(y, x)

print(ans)