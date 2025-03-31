from collections import deque
 
 
def bfs():
    start_candi = []
    for k in range(1, V + 1):
        if not graph2[k]:
            start_candi.append(k)
    q = deque()
    visited = [False] * (V + 1)
    visited[0] = True
    result = []
    for h in start_candi:
        q.append(h)
        visited[h] = True
        result.append(h)
 
    while q:
        x = q.popleft()
        for next_node in graph[x]:
            if visited[next_node]:
                continue
            graph2[next_node].discard(x)
            if not graph2[next_node]:
                q.append(next_node)
                visited[next_node] = True
                result.append(next_node)
        if False not in visited:
            return result
 
 
for t in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [set() for _ in range(V + 1)]
    graph2 = [set() for _ in range(V + 1)]
    for i in range(E):
        graph[arr[2 * i]].add(arr[2*i + 1])
        graph2[arr[2 * i + 1]].add(arr[2 * i])
    result = bfs()
    print(f'#{t}', *result)