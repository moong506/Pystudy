from collections import deque
import sys

def bfs(R):
    global cnt
    q = deque([R])
    visited[R] = cnt
    
    while q:
        v = q.popleft()
        
        for x in adj_list[v]:
            if visited[x] == 0:
                cnt += 1
                visited[x] = cnt
                q.append(x)
    
    
N, M, R = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
    
for i in range(N+1):
    adj_list[i].sort(reverse=True)
    
bfs(R)

for i in range(1, N+1):
    print(visited[i])
    