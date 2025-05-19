def bfs(adj_list, n):
    q = [1]
    visited = [0]*(n+1)
    visited[1] = 1
    
    while q:
        ti = q.pop(0)
        
        for ni in adj_list[ti]:
            if visited[ni] == 0:
                visited[ni] = visited[ti] + 1
                q.append(ni)
            elif visited[ni] > visited[ti] + 1:
                visited[ni] = visited[ti] + 1
                q.append(ni)
    count = 0
    max_num = 0
    for num in visited:
        if max_num < num:
            count = 1
            max_num = num
        elif max_num == num:
            count+=1
    return count

def solution(n, edge):
    answer = 0
    adj_list =[[] for _ in range(n+1)]
    
    for a, b in edge:
        adj_list[a].append(b)
        adj_list[b].append(a)
    answer = bfs(adj_list, n)
    return answer