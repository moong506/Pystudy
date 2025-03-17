def bfs(v, s):
    visited = [0] * (v+1)   # visited[0]는 비어 있는 개념
    q = [s]     # 시작점을 q에 추가
    visited[s] = 1  # 시작점은 방문한 것으로 기록
    print(s, end = ' ')
    while q:
        t = q.pop(0)    # queue에서 앞 요소를 꺼내와라
        for k in arr[t]:    # t에 인접한 k를 돌면서
            if visited[k] == 0: # 방문하지 않았다면
                q.append(k) # queue에 넣고
                visited[k] = 1 # 방문했다고 표기한다
                print(k, end = ' ')
            # else:   # 방문했으면 냅둬

# 인접해서 넘어갈 수 있으면 넘어가기 전에 본인의 위치를 stack에 기록해라   이동불가면 뒤로 돌아가라
def dfs(v, s):
    visited = [0] * (v+1)
    stack = []
    while True:
        if visited[s] == 0: # 넘어왔으면 방문했다고 기록해라
            visited[s] = 1
            print(s, end = ' ')
        for k in arr[s]:
            if visited[k] == 0:
                stack.append(s)
                s = k
                break   # 이동했으면 인접요소 그만 찾고 break
        else:       # for-else: break 없이 작동했으면 == 이동불가면     팝해서 그 위치로 돌아가라
            if stack:   # 스택이 있다면
                s = stack.pop()
            else:
                break   #while 문 종료
    print()


V, E, S = map(int, input().split())
arr = [[] for _ in range(V+1)]
# 인접한 정점들 기록
for _ in range(E):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)
# 이 과정 차이점
for i in range(V+1):
    arr[i].sort()

dfs(V, S)
bfs(V, S)
