def find_route(node):
    global cnt

    if node == goal: # 도착한 경우
        cnt += 1
        return

    if graph[node]: # 리프노드가 아닌 경우
        for i in graph[node]: # node에서 갈 수 있는 정점 i
            if visited[i] == 1: # 이미 방문한 거면
                continue
            visited[i] = 1
            find_route(i) # i로 재귀
            visited[i] = 0
    else:
        return


T =int(input())
for tc in range(1,T+1):

    last, edge = map(int,input().split())
    arr = list(map(int,input().split()))

    graph =[[] for _ in range(last+1)]

    for i in range(edge):
        graph[arr[i*2]].append(arr[i*2+1])

    start, goal = map(int,input().split())

    cnt = 0
    visited = [0] * (last+1)
    find_route(start)
    print(f'#{tc} {cnt}')