'''
Python은 기본적으로 재귀 깊이에 제한이 있는데, 
이 문제에서는 노드 수(N)가 많을 경우 이 제한을 초과할 수 있습니다.
'''

import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 늘리기

def dfs(R):
    global order
    visited[R] = order
    adj_node[R].sort(reverse=True)  # 내림차순으로 방문

    for x in adj_node[R]:
        if visited[x] == 0:
            order += 1
            dfs(x)


N, M, R = map(int, sys.stdin.readline().split())
adj_node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
order = 1

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_node[u].append(v)  # 양방향 간선
    adj_node[v].append(u)  # 양방향 간선

dfs(R)

for i in range(1, len(visited)):
    print(visited[i])