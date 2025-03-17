import sys
sys.setrecursionlimit(10**6)

def dfs(R):  # 깊이 탐색 함수
    global cnt
    visited[R] = cnt
    adj_list[R].sort()

    for x in adj_list[R]:
        if visited[x] == 0:
            cnt += 1
            dfs(x)


N, M, R = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]  # 인접한 노드
visited = [0] * (N+1)  # 방문 여부 표시
cnt = 1


for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    # 양방향
    adj_list[u].append(v)
    adj_list[v].append(u)

dfs(R)

for i in range(1, len(visited)):
    print(visited[i])