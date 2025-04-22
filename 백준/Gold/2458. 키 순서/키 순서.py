def count_height(adj):
    count = [0]*(N+1)
    for idx in range(1, N+1):
        stack = [0] * (N + 1)
        top = 0
        stack[top] = idx
        visited = [0]*(N+1)
        while top >= 0:
            ti = stack[top]
            top -= 1
            for item in adj[ti]:
                if visited[item] == 0:
                    visited[item] = 1
                    top += 1
                    stack[top] = item
                    count[item] += 1
    return count


N, M = map(int, input().split())
adj_up = [[] for _ in range(N+1)]
adj_down = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_up[a].append(b)
    adj_down[b].append(a)

ans1 = count_height(adj_up)
ans2 = count_height(adj_down)

ans = 0
for i in range(1, N+1):
    if ans1[i] + ans2[i] == N-1:
        ans += 1
print(ans)