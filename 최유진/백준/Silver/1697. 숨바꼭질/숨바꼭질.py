from collections import deque

def hide_and_seek(n, k):
    visited = [0] * 100001  # 각 위치에 도달하는 최소 시간을 저장 (0이면 미방문)
    q = deque()
    q.append(n)
    visited[n] = 1  # 시작 위치는 1로 표시 (최종 출력 시 1을 빼줌)

    while q:
        now = q.popleft()
        if now == k:
            return visited[now] - 1  # 시작점을 1부터 세었으므로 1 빼줌
        for next in (now - 1, now + 1, now * 2):
            if 0 <= next < 100001 and visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)


N, K = map(int, input().split())
print(hide_and_seek(N, K))
