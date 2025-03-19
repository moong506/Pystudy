def check(row,col):
    for i in range(row):
        if visited[i][col] == 1:
            return False
    # 대각선은 기울기로 접근해보겠다...
    # 재귀 걸리는 순서보면 위에서 부터 아래로 내려온다
    # 따라서 대각선 확인 방면은 아래서 위로만 하면 된다
    # 근데 여기선 다 해
    for i in range(N):
        for j in range(N):
            if (col - j) != 0 and abs((row-i)/(col-j)) == 1 and visited[i][j] == 1:
                return False
    return True


def f(i,N):
    global ans
    if i == N:
        ans += 1
        return
    else:
        for j in range(N):
            if check(i,j):
                visited[i][j] = 1
                f(i+1,N)
                visited[i][j] = 0


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    ans = 0
    f(0,N)
    print(f'#{tc} {ans}')