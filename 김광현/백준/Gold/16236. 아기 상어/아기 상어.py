# 함수를 만들었지만 while문을 2번 돌려도 됩니다!
# BFS를 만드는 경우에 한 번, 그리고 그 BFS를 통해서 다음 먹이의 위치를 찾는 경우에 한 번 해서 반복
def find_start(n, lst):  # 처음 아기 상어의 위치 찾기
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 9:
                return i, j

def bfs(x, y, n, lst):  # visited 배열을 구하기 위한 BFS
    visited = [[-1] * n for _ in range(n)]
    q = [[0, 0]] * (n * n)
    front = -1
    rear = 0
    q[rear] = [x, y]
    visited[x][y] = 0  # 최소 거리를 구하기 위해서 처음 visited를 0으로 설정
    lst[x][y] = 0
    while front != rear:
        front += 1
        i, j = q[front]
        for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and size >= arr[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                rear += 1
                q[rear] = [ni, nj]
    return visited
# 다음 먹이를 찾는 find_prey 함수
# 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기
# 그러한 물고기가 여러 마리라면 가장 왼쪽에 있는 물고기
# 이를 간단하게 제일 짧은 것 중에 for문을 통해서 작은 것을 찾으면 됨.
# min_prey_dis > visited[i][j]: 조건을 통해서 가장 위(i중에서) 가장 왼쪽(j)를 구함

def find_prey(visited, n, lst):
    x, y = 0, 0
    min_prey_dis = float('inf')
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 1 <= lst[i][j] < size:
                if min_prey_dis > visited[i][j]:
                    min_prey_dis = visited[i][j]
                    x, y = i, j
    if min_prey_dis == float('inf'):
        return False
    else:
        return x, y, min_prey_dis  # 최소 거리를 구함

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2
ans = 0
cnt = 0
stx, sty = find_start(N, arr)
while True:
    result = find_prey(bfs(stx, sty, N, arr), N, arr)
    if not result:  # 더 이상 갈 곳이 없다면
        print(ans)  # 결과를 프린트
        break
    else:  # 갈 곳이 있으면 그 위치로 이동
        stx, sty = result[0], result[1]
        ans += result[2]
        arr[stx][sty] = 0
        cnt += 1
    if cnt >= size:  # 상어의 크기 조정
        size += 1
        cnt = 0