def dfs(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                cnt = 1
                for di, dj in [[1,0],[1,-1],[0,1],[0,-1],[1,1],[-1,-1],[-1,0],[-1,1]]:
                    for c in range(1, 5):
                        ni, nj = i+di*c, j+dj*c
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] != '.':
                            cnt += 1
                            if cnt == 5:
                                return 'YES'
                        else:
                            cnt = 1
                            break       # for c
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    result = dfs(arr, N)

    print(f'#{tc} {result}')