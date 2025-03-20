import heapq


# 다익스트라 알고리즘을 사용하여 start_node 에서 end_node 까지의 최단 거리를 계산하는 함수.
'''
시간을 줄여보자!!
O(N * ( E logV))의 시간 복잡도를 가지던 코드를
만약 reversed_graph 를 만들어서 미리 dijkstra 를 실행해서 저장해두면,
O(2 * ( E logV)) 로 시간 복잡도를 줄일 수 있다!!
reversed 를 통해서 dijkstra 함수를 돌리면 X에서 가는 최소 길이가 아닌
X로 오는 최소 길이를 알 수 있다.
'''


def dijkstra(start_node, arr):  # (출발 노드, 도착점들의 리스트)를 매개변수로 설정
    pq = [(0, start_node)]  # (거리, 노드) 형태의 우선순위 큐
    distance = [float('inf')] * (N + 1)  # 모든 노드까지의 거리 무한대
    distance[start_node] = 0  # 출발 노드의 거리는 0

    while pq:
        min_dis, x = heapq.heappop(pq)  # 현재까지의 최단 거리와 노드 번호 가져오기

        if distance[x] < min_dis:  # distance[x]보다 길어지면 무시
            continue

        # 현재 노드에서 이동할 수 있는 인접 노드 탐색
        for dis, next_village in arr[x]:
            new_dis = min_dis + dis  # 새로운 거리 계산
            if distance[next_village] > new_dis:  # 더 짧은 거리라면 업데이트
                distance[next_village] = new_dis
                heapq.heappush(pq, (new_dis, next_village))  # 우선순위 큐에 추가

    return distance  # 최단 거리 리스트를 반환


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]  # 역방향 그래프

    for _ in range(M):  # 간선 정보 입력 (방향 그래프)
        u, v, w = map(int, input().split())  # u에서 v로 가는 가중치 w인 간선
        graph[u].append([w, v])
        reverse_graph[v].append((w, u))

    # 1. X에서 모든 노드까지 최단 거리 리스트
    from_X_lst = dijkstra(X, graph)

    # 2. 모든 노드에서 X까지 최단 거리 리스트
    to_X_lst = dijkstra(X, reverse_graph)

    # 3. 왕복 거리를 계산해서 최대 값을 추출
    max_result = 0
    for i in range(1, N + 1):
        if i != X:
            result = from_X_lst[i] + to_X_lst[i]  # 왕복 거리 계산
            max_result = max(max_result, result)  # 최댓값 갱신
    print(f'#{tc} {max_result}')
