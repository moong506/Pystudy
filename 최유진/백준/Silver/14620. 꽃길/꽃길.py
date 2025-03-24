def dfs(cnt, current_c):
    global min_val
    if cnt == 3:        # 3번 심으면 그게 정답
        min_val = min(min_val, current_c)   # 둘 중 작은게 정답

    if current_c >= min_val:    # 이미 넘어버리면 return
        return
    
    for i in range(1, N-1):         # 인덱스에러 미리 방지
        for j in range(1, N-1):
            # 꽃 심을 구간 다섯개
            plant = [[i, j], [i+1, j], [i, j+1], [i-1, j], [i, j-1]]
            one_c = 0       # 하나 심는 비용
            for ni, nj in plant:
                if visited[ni][nj]: # 방문했다면? 멈춰
                    break
                one_c += cost[ni][nj]
            else:   # 다 돌고 나서
                for ni, nj in plant:
                    visited[ni][nj] = 1     # 방문 처리
                dfs(cnt+1, current_c+one_c) # 재귀 처리
                for ni, nj in plant:
                    visited[ni][nj] = 0     # 원복


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
min_val = N*N*200

dfs(0, 0)
print(min_val)