import sys
input = sys.stdin.readline

def prim(s):
    INF = 10001
    visited = [0] * (N + 1)     # MST에 포함된 노드들, 인덱스를 위해 (N+1)개
    weight = [INF] * (N + 1)    # 각 노드별 MST에 포함될 때의 소비한 가중치, 인덱스를 윌해 (N+1)개

    weight[s] = 0               # 시작노드는 가중치 0
    for _ in range(N):          # 총 N개의 노드를 MST에 포함시킬 때까지 반복

        # MST에 넣을 노드 선택 (MST에 인접한 노드 중 가장 가중치가 작은 것)
        mn = INF
        i_min = 0
        for i in range(1, N + 1):   # 모든 노드를 돌면서, 인접하고 & 가중치가 가장 작은 것
            if not visited[i] and weight[i] < mn:
                mn = weight[i]
                i_min = i
        visited[i_min] = 1          # MST에 포함

        # 새로 MST에 추가된 노드에 대해서 인접 노드 가중치 최솟값으로 업데이트
        for w, adj in adjLst[i_min]:
            if not visited[adj] and weight[adj] > w:    # MST의 인접노드이며 & 최솟값일 경우 업데이트
                weight[adj] = w

    print(sum(weight[1:]))      # 임의로 추가한 0번 인덱스외의 값을 더해서 출력

N = int(input())
M = int(input())

adjLst = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j, w = map(int, input().split())
    adjLst[i].append((w, j))
    adjLst[j].append((w, i))
prim(1)