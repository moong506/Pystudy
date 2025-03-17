from collections import deque
import sys

def bfs(R):
    global cnt
    q = deque([R])  # 시작점을 큐에 넣음

    visited[R] = cnt

    while q:
        v = q.popleft()

        for i in adj_list[v]:
            if visited[i] == 0:
                q.append(i)
                cnt += 1
                visited[i] = cnt


N, M, R = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)  # 양방향 간선
    adj_list[v].append(u)  # 양방향 간선

for i in range(N+1):
    adj_list[i].sort()

bfs(R)

for i in range(1, len(visited)):
    print(visited[i])