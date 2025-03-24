def dijkstra():
    visited = [21e10] * (N+1)
    while q:
        cost, end = heapq.heappop(q)
        if visited[end] < cost:
            continue
        for next_w, next_e in graph[end]:
            new_cost = next_w + cost
            if visited[next_e] > new_cost:
                visited[next_e] = new_cost
                heapq.heappush(q, (new_cost, next_e))
    return visited[G]


import heapq
N = int(input())    # 도시 개수 (노드)
M = int(input())    # 버스 개수 (간선)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e ,w = map(int, input().split())
    graph[s].append((w,e))
S ,G = map(int, input().split())
q = [(0,S)]

# print(graph)
print(dijkstra())
