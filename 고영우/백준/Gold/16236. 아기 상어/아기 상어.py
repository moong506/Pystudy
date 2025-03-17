N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start_i = start_j = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start_i = i
            start_j = j
            arr[i][j] = 0
shark_size = 2
shark_size_idx = 0
total_cnt = 0
q = [(start_i, start_j)]
ans = 0
while True:
    real_place_i = 0
    real_place_j = 0
    visited = [[0]*N for _ in range(N)]
    new_place = []
    visited[start_i][start_j] = 1
    while q:
        t = q.pop(0)
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = t[0]+ di, t[1] + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]<= shark_size and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[t[0]][t[1]] + 1
                if arr[ni][nj] < shark_size and arr[ni][nj]!=0:
                    new_place.append((ni,nj))

    if not new_place:
        ans = total_cnt
        break
    real_place_i = new_place[0][0]
    real_place_j = new_place[0][1]
    for i in range(len(new_place)):
        j = 1
        if visited[new_place[i][0]][new_place[i][1]] < visited[real_place_i][real_place_j]:
            real_place_i = new_place[i][0]
            real_place_j = new_place[i][1]
        elif visited[new_place[i][0]][new_place[i][1]] == visited[real_place_i][real_place_j]:
            if new_place[i][0] < real_place_i:
                real_place_i = new_place[i][0]
                real_place_j = new_place[i][1]
            elif new_place[i][0] == real_place_i:
                if new_place[i][1] < real_place_j:
                    real_place_i = new_place[i][0]
                    real_place_j = new_place[i][1]
    total_cnt += visited[real_place_i][real_place_j] -1
    arr[real_place_i][real_place_j] = 0
    q.append((real_place_i, real_place_j))
    shark_size_idx += 1
    if shark_size_idx == shark_size:
        shark_size += 1
        shark_size_idx = 0
    start_i = real_place_i
    start_j = real_place_j
print(total_cnt)