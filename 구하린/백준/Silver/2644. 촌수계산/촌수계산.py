from collections import deque
N = int(input())

tar1, tar2 = map(int, input().split()) # parent, child는 상관 없이 연결되면 촌수 계산 가능 
M = int(input())

family_graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    family_graph[x].append(y) 
    family_graph[y].append(x) # parent, child는 상관 없이 연결되면 촌수 계산 가능하니까 양방향으로 저장

# 가계도 작성 끝

que = deque()
que.append(tar1)
visited = [0] * (N+1)
visited[tar1] = 1
ans = -1 # que가 다 끝나도 타겟 발견 못할 경우

while que:
    start = que.popleft()
    connected = family_graph[start]

    if start == tar2:
        ans = visited[start] - 1
        break
    for child in connected:
        if visited[child] == 0:
            que.append(child)
            visited[child] = visited[start] + 1

print(ans)