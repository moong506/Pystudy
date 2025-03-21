import heapq

def prim(tax):
    pq = [(0, 0)]
    visited = [0] * N
    min_cost = 0
    
    dists = [float('inf')] * N      # 최소비용 저장 리스트
    dists[0] = 0                # 시작점 비용은 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue

        # node로 가는 간선을 확정짓는 코드
        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            # ((x좌표 사이^2) + (y좌표 사이^2)) * tax
            new_cost = ((x_lst[next_node]-x_lst[node])**2 + (y_lst[next_node]-y_lst[node])**2) * tax
            
            # 우선순위큐에 삽입된 거리를 저장하면서 진행
            # 더 작은 비용으로 갈 수 있을 때만 heapq에 삽입
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{tc} {result}')