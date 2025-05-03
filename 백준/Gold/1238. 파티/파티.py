import sys
# input = sys.stdin.readline
import heapq

def dij1(sti):
    cost = [float('Inf')]*(N+1)
    cost[0] = 0
    cost[sti] = 0
    pq = [[0, sti]]
    while pq:
        weight, node = heapq.heappop(pq)

        if cost[node] < weight:
            continue

        for next_cost, next_node in arr[node]:
            if cost[next_node] > next_cost + weight:
                cost[next_node] = next_cost + weight
                heapq.heappush(pq, [cost[next_node], next_node])

    return cost

def dij2(sti, end):
    cost = [float('Inf')] * (N + 1)
    cost[sti] = 0
    pq = [[0, sti]]
    while pq:
        weight, node = heapq.heappop(pq)

        if cost[node] < weight:
            continue
        if node == end:
            return cost[end]

        for next_cost, next_node in arr[node]:
            if cost[next_node] > next_cost + weight:
                cost[next_node] = next_cost + weight
                heapq.heappush(pq, [cost[next_node], next_node])




N, M, X = map(int,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int,input().split())
    arr[s].append([t, e])

# 돌아오는 길이랍니다!
ans = dij1(X)

for i in range(1,N+1):
    if i == X:
        continue
     # 마을까지 갑시다!
    new_cost = dij2(i, X)
    ans[i] += new_cost

print(max(ans))
