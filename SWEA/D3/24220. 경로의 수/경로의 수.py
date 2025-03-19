def dfs(s,g,visited):
    global count

    visited[s]=1
    if s==g: # 도착점에 도착
        count+=1 # 경우의 수 하나 추가
        return

    for w in adj_list[s]: # 인접 노드에 방문
        if visited[w]==0:
            dfs(w,g,visited[:]) # 백트래킹


T=int(input())
for tc in range(1,T+1):
    # 정점번호 N과 간선 수 E
    N,E=map(int,input().split())
    arr=list(map(int,input().split()))
    # 출발 정점 S와 도착 정점 번호G
    S,G=map(int,input().split())

    visited=[0]*(N+1)

    # 인접 리스트 생성
    adj_list = [[] for _ in range(N + 1)]
    for i in range(E):
        left=arr[i*2]
        right=arr[i*2+1]
        adj_list[left].append(right) # 단방향

    count=0
    dfs(S,G,visited)
    print(f'#{tc} {count}')