import sys
import heapq

def dijkstra(start_node):
    pq = [(0,start_node)]
    dists = [100001000] * (N+1)
    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue
            else:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist,next_node))
    return dists


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, price = map(int, sys.stdin.readline().split())

    graph[start].append((price, end))

S,G = map(int, input().split())

if S == G:
    print(0)
else:
    result_dists = dijkstra(S)
    print(result_dists[G])