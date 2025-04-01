def dijkstra():
    while q:
        cnt, end = heapq.heappop(q)
        if visited[end] < cnt:
            continue
        for next_e in graph[end]:
            new_cnt = cnt + 1
            if visited[next_e] > new_cnt:
                visited[next_e] = new_cnt
                heapq.heappush(q, (new_cnt, next_e))
    return visited

import heapq
N, M, K, X = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
visited = [21e10] * (N+1)
q = [(0,X)]
dijkstra()

ans = []
for i in range(1,N+1):
    if visited[i] == K and i != X:
        ans.append(i)

ans.sort()
if ans:
    for i in ans:
        print(i)
else:
    print(-1)
