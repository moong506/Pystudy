def f(i, per):
    global max_p
    if i >= N:
        if max_p < per:
            max_p = per
        return
    elif per <= max_p:
        return
    else:
        for j in range(N):
            if did[j] == 1:
                continue
            else:
                did[j] = 1
                f(i + 1, per * P[i][j])
                did[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    max_p = 0
    did = [0] * N
    f(0,1)
    print(f'#{tc} {max_p*100:.6f}')