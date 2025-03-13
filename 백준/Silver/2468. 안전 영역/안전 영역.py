from collections import deque
def bfs():
    max_area = 0
    for k in range(M):
        cnt = 0
        visited = set()
        for i in range(N):
            for j in range(N):
                if (i, j) in visited or rain[i][j] <= k:
                    continue
                q = deque([(i, j)])
                visited.add((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and rain[nx][ny] > k and (nx, ny) not in visited:
                            q.append((nx, ny))
                            visited.add((nx, ny))
                cnt += 1
        max_area = max(max_area, cnt)
    return max_area


N = int(input())
rain = [list(map(int, input().split())) for _ in range(N)]
max_area = 0
M = max(sum(rain, []))
print(bfs())