import sys
from collections import deque

def get_result():
    global tomato # 토마토 배열 자체에 입력할게요 

    days = 0

    while que: # 익힐 토마토 목록이 있는 동안
        k, p = que.popleft()

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = k + di
            nj = p + dj

            if 0<=ni<N and 0<=nj<M and tomato[ni][nj] == 0: # 델타가 범위 안이고 아직 안 익은 토마토면
                if tomato[ni][nj] == 0:
                    tomato[ni][nj] = tomato[k][p] + 1 # 일수 계산을 위해
                    que.append((ni, nj))

    # BFS 끝
    # 안 익은 토마토 있는지 검사
    for q in range(N):
        if 0 in tomato[q]: # 안 익은 토마토가 있으면
            return -1
        elif days < max(tomato[q]): # max값 갱신해야하면
            days = max(tomato[q])
    return days - 1 # 첫째날부터 1이라서 걸린 날이니까 하나 빼줘야 함


M, N = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(tomato)
que = deque()


for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            que.append((i, j))
# 초기에 익은 토마토 파악 끝
# 토마토 익히기 시작
ans = get_result()

print(ans)
