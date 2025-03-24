import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, w = map(int,input().split())
    graph[u].append([w, v])
start, end = map(int, input().split())

pq = [(0, start)]
dists = [float('inf')] * (N + 1)
dists[start] = 0

while pq:
    dist, node = heapq.heappop(pq)

    if dists[node] < dist:
        continue

    for next_dist, next_node in graph[node]:
        new_dist = dist + next_dist

        if new_dist < dists[next_node]:
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

print(dists[end])