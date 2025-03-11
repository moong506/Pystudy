from collections import deque


def dfs(V):
    global order
    visited1[V] = order
    print(V, end=" ")  # V부터 방문된 점을 순서대로 출력

    for x in adj_list[V]:
        if visited1[x] == 0:
            order += 1
            visited1[x] = order
            dfs(x)


def bfs(V):
    order = 1
    q = deque([V])
    visited2[V] = order

    while q:
        v = q.popleft()
        print(v, end=" ")  # V부터 방문된 점을 순서대로 출력

        for x in adj_list[v]:
            if visited2[x] == 0:
                order += 1
                visited2[x] = order
                q.append(x)


N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(N+1):
    adj_list[i].sort()

order = 1
dfs(V)

print()

bfs(V)
