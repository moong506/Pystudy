import heapq  # 우선순위 큐를 사용하기 위한 heapq 모듈 임포트


def dijkstra(start_node, end_node):
    # 시작 노드와 비용(0)을 우선순위 큐에 삽입
    pq = [(0, start_node)]  # (비용, 노드) 형태로 저장
    costs = [float('inf') for _ in range(N+1)]  # 각 노드까지의 최소 비용을 저장할 배열
    costs[start_node] = 0  # 시작 노드의 비용은 0으로 설정

    while pq:  # 우선순위 큐가 비어있지 않은 동안 반복
        cost, node = heapq.heappop(pq)  # 현재 최소 비용을 가진 노드 추출

        # 이미 처리된 노드라면 패스 (더 짧은 경로를 이미 찾은 경우)
        if costs[node] < cost:
            continue

        # 현재 노드와 연결된 모든 간선 확인
        for next_node, next_cost in bus[node]:

            # 현재 노드를 거쳐 다음 노드로 가는 비용 계산
            new_cost = cost + next_cost

            # 기존 비용보다 현재 경로를 통한 비용이 더 크거나 같다면 패스
            if costs[next_node] <= new_cost:
                continue

            # 더 작은 비용을 발견했다면 갱신
            costs[next_node] = new_cost
            # 우선순위 큐에 새로운 노드와 새로운 비용 추가
            heapq.heappush(pq, (new_cost, next_node))

    # 도착 노드까지의 최소 비용 반환
    return costs[end_node]


N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]

for _ in range(M):
    start_city, end_city, cost = map(int, input().split())
    bus[start_city].append([end_city, cost])

start, end = map(int, input().split())

answer = dijkstra(start, end)

print(answer)
