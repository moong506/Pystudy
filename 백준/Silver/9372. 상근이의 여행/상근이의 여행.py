from collections import deque


def bfs(start_node):
    q = deque()
    q.append(start_node)

    cnt = 0

    while q:
        node = q.popleft()
        visited[node] = 1

        for next_node in adj_list[node]:
            if visited[next_node] == 0:
                q.append(next_node)
                visited[next_node] = 1
                cnt += 1

    return cnt


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())

        adj_list[a].append(b)
        adj_list[b].append(a)

    answer = bfs(1)

    print(answer)
