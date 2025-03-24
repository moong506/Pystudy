def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]
 
def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))     # 섬의 x좌표
    y_lst = list(map(int, input().split()))     # 섬의 y좌표
    tax = float(input())    # 환경 부담 세율
 
    parents = [i for i in range(N)]
    min_cost = 0
 
    # 1. 간선 정보 저장
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            cost = ((x_lst[i]-x_lst[j])**2 + (y_lst[i]-y_lst[j])**2) * tax
            edges.append((i, j, cost))
 
    # 2. 가중치 기준 오름차순 정렬
    edges.sort(key = lambda x: x[2])
 
    # 3. 앞에서부터 간선 검사하면서, 사이클 유무 검사 (N-1)개의 간선을 선택하면 종료
    cnt = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            min_cost += w
            cnt += 1
        if cnt == N-1:
            break
 
    print(f'#{tc} {min_cost: .0f}')