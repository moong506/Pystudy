import heapq

def dij():
    cost = [5e7] * (N+1)
    cost[1] = 0

    pq = [[0, 1]]

    while pq:
        weight, idx = heapq.heappop(pq)

        if cost[idx] < weight:  # 미리 가지치기
            continue

        for next_cost, next_idx in adj[idx]:
            if cost[next_idx] > weight + next_cost:  # 더 작은 길 찾았당!
                cost[next_idx] = weight + next_cost
                heapq.heappush(pq, [cost[next_idx], next_idx])
    return cost[N]

N, M = map(int, input().split())
adj = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

ans = dij()
print(ans)