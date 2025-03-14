T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = cnt = min_num = 0
    sequence = [0] * (N*N +1)

    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni = i + di
                nj = j + dj
        
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == arr[i][j] + 1:
                        sequence[arr[i][j]] = 1
                        break # 숫자가 어차피 다 달라서 찾으면 break
                        
    for idx in range(1, N*N+1):
        if sequence[idx]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                min_num = idx - cnt
            cnt = 0

    print(f'#{tc} {min_num} {max_cnt+1}')