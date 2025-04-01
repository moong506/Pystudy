def find_distance(p):
    visited = [[0] * N for _ in range(N)]
    distance = 0
    q = []
    for i,j in p:
        visited[i][j] = 1
        q.append((i,j))
    while q:
        ti, tj = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ti][tj] + 1
                q.append((ni,nj))
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                distance += visited[i][j] - 1
    return distance


def combination(i,start):
    global min_distance
    if i == M:
        min_distance = min(min_distance, find_distance(chicken_combination))
        return

    for j in range(start,chicken_cnt):
        chicken_combination.append(chicken[j])
        combination(i+1,j+1)
        chicken_combination.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr에 있는 치킨집에서 M개의 조합을 구해서 합을 비교해서 최소값을 찾자
chicken = []
chicken_combination = []
chicken_cnt = 0
min_distance = 21e10
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i,j))
            chicken_cnt += 1
combination(0,0)
print(min_distance)