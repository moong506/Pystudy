# 간선의 수가 많으므로 prim을 사용해보자
def prim(E):
    pq=[(0,0)]  # 비용,노드번호 순서로 저장.
    visited=[0]*N # visited
    min_cost=0 # 최소 비용 저장

    dist=[float('inf')]*N # 최소 비용 저장 리스트
    dist[0]=0 # 시작점의 비용은 0

    while pq:
        cost,node=heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if visited[node]:
            continue

        visited[node] = 1  # 방문처리
        min_cost += cost  # 누적한 추가

        for m in range(N):
            if visited[m]: # 만약 방문했으면 다음 섬 탐색
                continue

            new_cost=((x_idx[m]-x_idx[node])**2+(y_idx[m]-y_idx[node])**2)*E

            if new_cost<dist[m]:
                dist[m]=new_cost
                heapq.heappush(pq,(new_cost,m))

    return round(min_cost)


import heapq
T=int(input())
for tc in range(1,T+1):
    N=int(input()) # 섬의 수
    x_idx=list(map(int,input().split()))
    y_idx=list(map(int,input().split()))
    E=float(input())

    result=prim(E)
    print(f'#{tc} {result}')