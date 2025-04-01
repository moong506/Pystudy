def prim(s):
    q = [(0,s)]
    visited = [0] * (V+1)
    min_weight = 0
    while q:
        weight, node = heapq.heappop(q)
        if visited[node]:
            continue
        visited[node] = 1
        min_weight += weight
        for next_w, next_n in adjL[node]:
            if visited[next_n] == 0:
                heapq.heappush(q, (next_w, next_n))
    return min_weight

import heapq
V = int(input())
E = int(input())
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adjL[s].append((w,e))
    adjL[e].append((w,s))
print(prim(1))