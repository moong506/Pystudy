# 네트워크 연결(Prim)
# 주의해야할 가정: a와b가 같을 수 있다(이건 그냥 무시해도 됨. 최소가 아니므로)
def prim(start_node):
    pq=[(0,start_node)]
    MST=[0]*(V+1)
    min_weight=0

    while pq:
        weight,node=heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue

        # 아니라면
        MST[node]=1 # 방문표시 하고
        min_weight+=weight # 가중치 더하고

        for next_node in range(1,V+1):
            # 만약 갈 수 없으면
            if graph[node][next_node]==0:
                continue
            # 이미 방문했으면
            if MST[next_node]:
                continue
            # 위의 둘다 아니면
            heapq.heappush(pq,(graph[node][next_node],next_node))
    return min_weight

import heapq
V=int(input()) # 정점의 수
E=int(input()) # 간선의 수
graph = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result=prim(1)
print(result)

# # Kruskal
# def find_set(x):
#     if x==parents[x]:
#         return x
#     parents[x]=find_set(parents[x])
#     return parents[x]
#
# def union(x,y):
#     ref_x=find_set(x)
#     ref_y=find_set(y)
#
#     if ref_x==ref_y:
#         parents[ref_y]=ref_x
#     else:
#         parents[ref_x]=ref_y
#
# import heapq
# V=int(input()) # 정점의 수
# E=int(input()) # 간선의 수
# edges=[] # 간선의 정보
# for _ in range(E):
#     start, end, weight = map(int, input().split())
#     edges.append((start, end, weight))
#
# # 가중치 기준으로 정렬
# edges.sort(key=lambda x:x[2])
# parents=[i for i in range(V+1)]
#
# cnt=0
# result=0
# for u,v,w in edges:
#     if find_set(u)!=find_set(v):
#         union(u,v)
#         cnt+=1
#         result+=w
#
#         if cnt==V-1:
#             break
#
# print(result)