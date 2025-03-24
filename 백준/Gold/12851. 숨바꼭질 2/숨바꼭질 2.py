# 숨박꼭질 2
# 앞선 1697 숨박꼭질에서 최소시간이 걸리는 경로의 수를 추가적으로 구하는 문제이다.
def bfs(start,end):
    min_time=float('inf')
    q=deque([(start,0)]) # 수빈이의 위치, 소요 시간
    visited = [0] * 100001 # 갔던 위치를 다시 방문하게 하지 않기 위함
    visited[start]=0 # 시작 위치에서 시간은 0
    count=0
    min_time=-1

    while q:
        loc,time=q.popleft() # 현재 위치와 소요 시간

        # 이미 최소 시간을 찾았고, 현재 시간이 최소 시간보다 크면 더 이상 탐색할 필요 없음
        if min_time != -1 and time > min_time:
            break

        if loc==end: # 도착점에 도착하면
            if min_time ==-1:
                min_time=time # min_time 업데이트. 처음 방문한 경우

            if time==min_time:
                count+=1
            continue

        # 다음 위치 탐색
        for next_loc in [loc + 1, loc - 1, loc * 2]:
            # 범위 체크
            if 0 <= next_loc <= 100000:
                # 방문하지 않았거나, 같은 시간에 방문하는 경우
                if visited[next_loc] == 0 or visited[next_loc] == time + 1:
                    visited[next_loc] = time + 1
                    q.append((next_loc, time + 1))

    return min_time,count


from collections import deque
N,K=map(int,input().split())
min_time,final_count= bfs(N, K)
print(min_time)    # 최소 시간
print(final_count)
