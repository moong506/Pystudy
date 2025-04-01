import heapq

def prim(start):
    # 방문 여부
    visited = [False] * (N + 1)
    # 최소 힙 (우선순위 큐)
    min_heap = []
    # 최소 비용
    total_cost = 0
    # (비용, 정점)
    heapq.heappush(min_heap, (0, 1))
    while min_heap:
        cost, now = heapq.heappop(min_heap)
        # 이미 방문한 노드라면
        if visited[now]:
            continue
        # 방문 처리
        visited[now] = True
        # 최소 비용 추가
        total_cost += cost
        # 현재 노드와 연결된 다른 노드들을 최소 힙에 추가
        for edge_cost, next_node in graph[now]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (edge_cost, next_node))
    return total_cost

N = int(input())
M = int(input())
# 인접 리스트
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))
print(prim(1))