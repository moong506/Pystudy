def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y
 
def find_set(x):
    while parents[x] != x:
        x = parents[x]
    return x
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    parents = [i for i in range(N)]
    min_cost = 0
    # 1. 간선들 정보를 모두 저장
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = ((x_list[i] - x_list[j]) ** 2 +
                    ((y_list[i] - y_list[j]) ** 2)) * E
            edges.append((i, j, cost))
    # 2. 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    # 3. 싸이클 검사하면서, 앞에서부터 간선을 연결한다
    # (N - 1)개의 간선이 선택될 때까지 반복
    count = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            min_cost += w
            count += 1
        if count == N - 1:
            break
    print(f"#{tc} {min_cost:.0f}")