from collections import deque

def bfs(N, K):
    q = deque()
    visited = [-1] * 1000001
    # 인큐
    q.append(N)
    visited[N] = 0
    while q:
        # 디큐
        w = q.popleft()
        if w == K:
            return visited[K]
        for next_w in (w - 1, w + 1, w * 2):
            if 0 <= next_w <= 1000000 and visited[next_w] == -1:
                # 인큐
                q.append(next_w)
                visited[next_w] = visited[w] + 1

N, K = map(int, input().split())
print(bfs(N, K))