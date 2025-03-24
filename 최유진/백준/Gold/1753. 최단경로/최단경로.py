# BOJ 1753
import heapq

def dijkstra(s_node):
    pq = [(0, s_node)]
    ds = [INF]*(V+1)
    ds[s_node] = 0      # 시작점 자신은 0

    while pq:
        d, node = heapq.heappop(pq)
        if ds[node] < d:
            continue

        for nex_info in graph[node]:
            next_d = nex_info[0]
            next_node = nex_info[1]
            new_d = d + next_d

            if ds[next_node] <= new_d:
                continue

            ds[next_node] = new_d
            heapq.heappush(pq, (new_d, next_node))

    return ds[1:]

INF = 2000001
V, E = map(int, input().split())
K = int(input())
s_node = K
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

result = dijkstra(K)
for i in range(V):
    if result[i] == INF:
        print('INF')
    else:
        print(result[i])