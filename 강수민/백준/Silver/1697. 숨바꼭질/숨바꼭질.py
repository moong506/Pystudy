def bfs(s, g):
    # 큐 생성
    q = [0] * 100000
    front = rear = -1

    # visited 생성
    visited = [0] * 100001

    # 시작점 인큐
    rear += 1
    q[rear] = s

    # 시작점 visited 표시
    visited[s] = 1

    # 큐에 원소가 남아있는 동안에 반복
    while front != rear:
        front += 1
        t = q[front]
        if t == g:      # 목표인 경우
            return visited[g] - 1

        # -1, +1, *2인 경우, 100000이하 자연수, 만든 적이 없는
        if t-1 > 0 and visited[t-1] == 0:
            rear += 1
            q[rear] = t-1
            visited[t-1] = visited[t] + 1
        if t+1 <= 100000 and visited[t+1] == 0:
            rear += 1
            q[rear] = t+1
            visited[t+1] = visited[t] + 1
        if t*2 <= 100000 and visited[t*2] == 0:
            rear += 1
            q[rear] = t*2
            visited[t*2] = visited[t] + 1

N, K = map(int, input().split())    # N 수빈이 위치 K 동생 위치
if K == 0:
    print(f'{N}')
else:
    ans = bfs(N, K)
    print(ans)