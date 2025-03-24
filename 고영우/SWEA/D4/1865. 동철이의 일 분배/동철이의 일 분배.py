def f(i,N,p):
    global max_probability
    if p <= max_probability:
        return
    if p == 0:
        return
    if i == N:
        if max_probability < p:
            max_probability = p
        return
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                f(i+1, N, p * arr[i][j])
                used[j] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # lambda로 받아오는게 킥이었음
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    used = [0] * N
    max_probability = 0
    f(0,N,1)
    print(f'#{tc} {round(max_probability * 100, 6):.6f}')