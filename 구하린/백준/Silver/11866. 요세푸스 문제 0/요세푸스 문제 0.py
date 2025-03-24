N, K = map(int,input().split())

arr = [i for i in range(N+1)] # 0부터 N까지
visited = [0] * (N+1) # 0번 인덱스부터 N번 인덱스까지

visited[0] = 1 # 0번  인덱스는 더미 값
rear = 1
deleted = 0
cnt = 0

print('<', end='')
while deleted<N-1:
    if visited[rear] == 0:
        cnt += 1
        if cnt == K:
            visited[rear] = 1
            print(f'{arr[rear]},', end=' ')
            deleted += 1
            cnt = 0
    rear += 1

    if rear == (N+1): # 범위 벗어남
        rear = 1 # 0번은 더미 값


# 삭제 안 된 숫자 하나 남음(deleted == N-1)
print(arr[visited.index(min(visited))],end='>')