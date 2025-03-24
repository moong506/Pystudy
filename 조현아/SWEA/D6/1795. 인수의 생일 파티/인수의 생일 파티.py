# dijkstra 이용.
def dijkstra(start):
    INF = int(21e8)
    pq=[(0,start)]  # (누적거리, 노드번호)
    dists=[INF]*(N+1)         # 각 정점까지의 최단 거리를 저장할 리스트
    dists[0]=0
    dists[start]=0   # 시작노드 최단거리는 0

    while pq:
        dist,node=heapq.heappop(pq)

        if dists[node]<dist:
            continue

        for next_info in graph[node]:
            next_dist=next_info[0] # 다음 노드로 가기 위한 가중치
            next_node=next_info[1] # 다음 노드 번호

            # 다음 노드로 가기 위한 누적거리
            new_dist=dist+next_dist

            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if dists[next_node]<=new_dist:
                continue

            # next_node 까지 도착하는 데 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists


import heapq
T=int(input())
for tc in range(1,T+1):
    N,M,X=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        # x: 출발노드, y: 도착노드, c: 시간
        x, y, c = map(int, input().split())
        graph[x].append((c,y))

    # 각자의 집에서 생일파티 집으로 가는 리스트
    result_party=[0]*(N+1)
    for i in range(1,N+1):
        result=dijkstra(i)
        result_party[i]=result[X]

    # X에서 출발해서 각자의 집으로 간 리스트
    result_home=dijkstra(X)

    total_result=[0]*(N+1)
    for i in range(1,N+1):
        total_result[i]=result_home[i]+result_party[i]
    final_final=max(total_result)
    print(f'#{tc} {final_final}')