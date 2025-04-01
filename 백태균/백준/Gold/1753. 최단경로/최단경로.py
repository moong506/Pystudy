import heapq  # 우선순위 큐를 위한 heapq 모듈 임포트
import sys


def dijkstra(start_node):
    costs[start_node] = 0  # 시작 노드의 비용을 0으로 초기화
    heap = [(0, start_node)]  # 우선순위 큐에 (비용, 노드) 형태롤 시작 노드 시작

    while heap:  # 힙이 비어있지 않는 동안 반복
        total, cur_node = heapq.heappop(heap)  # 현재 최소 비용을 가진 노드 추출

        if costs[cur_node] < total:  # 이미 처리된 노드라면 패스
            continue

        for cost, next_node in adj_node[cur_node]:  # 현재 노드와 연결된 모든 간선 확인
            next_cost = total + cost  # 시작점부터 다음 노드까지의 총 비용 계산

            if next_cost < costs[next_node]:  # 기존 경로보다 더 짧은 경로를 ㄹ발견한 경우
                costs[next_node] = next_cost  # 최소 비용 갱신
                heapq.heappush(heap, (next_cost, next_node))  # 힙에 새로운 (비용, 노드) 추가


input = sys.stdin.readline  # 입력 속도 향상

V, E = map(int, input().split())
K = int(input())  # 시작 정점
adj_node = [[] for _ in range(V + 1)]  # 인접 리스트 초기화 (각 노드에 연결된 간선 정보 저장)
costs = [float('inf')] * (V + 1)  # 각 노드까지의 최단 거리를 저장하는 배열, 무한대로 초기화

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_node[u].append((w, v))

dijkstra(K)


for i in range(1, V+1):
    if costs[i] == float('inf'):
        print("INF")
    else:
        print(costs[i])
