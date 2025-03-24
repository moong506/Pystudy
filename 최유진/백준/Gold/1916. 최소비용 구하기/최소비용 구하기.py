def dijkstra(s_node):
    pq = [(0, s_node)]  # (누적거리, 노드번호)
    ds = [INF] * N      # (각 정점까지 최단)누적거리 리스트 생성
    ds[s_node] = 0      # 시작노드 최단거리는 0

    while pq:
        d, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        if ds[node] < d:
            continue

        for next_info in graph[node]:
            next_d = next_info[0]       # 다음 노드 가기 위한 가중치
            next_node = next_info[1]    # 다음 노드 번호

            # 다음 노드로 가기 위한 누적 거리
            new_d = d + next_d
            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면
            if ds[next_node] <= new_d:
                continue
            # next_node 까지 도착하는데 비용은 new_d
            ds[next_node] = new_d
            heapq.heappush(pq, (new_d, next_node))

    return ds

import heapq
INF = int(21e8)

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    s -= 1
    e -= 1
    graph[s].append((w, e))
S, E = map(int, input().split())  # 출/도착
S -= 1
E -= 1
s_node = S

result_ds = dijkstra(s_node)
ans = result_ds[E]
print(ans)