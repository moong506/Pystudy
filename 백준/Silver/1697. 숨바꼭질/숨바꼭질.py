# BFS
def bfs(start,end):
    q=deque([(N,0)]) # 수빈이의 위치, 소요 시간
    visited = [0] * 100001 # 갔던 위치를 다시 방문하게 하지 않기 위함

    while q:
        loc,time=q.popleft() # 현재 위치와 소요 시간

        if loc==end: # 도착점에 도착하면
            return time
        if visited[loc]: # 방문한 적 있으면
            continue
        visited[loc]=1 # 방문 체크

        # 이동
        if loc + 1 <= 100000 and not visited[loc + 1]:# 가지치기+방문 여부 체크
            q.append((loc + 1, time + 1))
        if loc - 1 >= 0 and not visited[loc - 1]:
            q.append((loc - 1, time + 1))
        if loc * 2 <= 100000 and not visited[loc * 2]:
            q.append((loc * 2, time + 1))


from collections import deque
N,K=map(int,input().split())
visited=[0]*100001
print(bfs(N,K))