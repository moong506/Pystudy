import heapq


def dk():
    pq = [[0,start_node]]
    cost = [1000001*N] * (N+1)
    cost[start_node] = 0
    while pq:
        weight, node = heapq.heappop(pq)

        if cost[node] < weight:
            continue
        for next_weight, next_node in adj[node]:
            if cost[next_node] > next_weight + weight:
                cost[next_node] = next_weight + weight
                heapq.heappush(pq, [cost[next_node], next_node])
    return cost[end_node]


N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append([w, e])
start_node, end_node = map(int, input().split())

ans = dk()
print(ans)