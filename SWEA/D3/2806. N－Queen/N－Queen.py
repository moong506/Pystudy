# N-Queen
def check(row,col):
    # 열 체크
    for i in range(row):
        if visited[i][col]:
            return False

    # 왼쪽 대각선 체크
    i,j=row-1,col-1
    while i>=0 and j>=0:
        if visited[i][j]:
            return False
        i-=1
        j-=1

    # 오른쪽 대각선 체크
    i,j=row-1,col+1
    while i>=0 and j<N:
        if visited[i][j]:
            return False
        i-=1
        j+=1
    return True


def dfs(row):
    global answer
    if row==N:
        answer+=1
        return

    for col in range(N):
        if not check(row,col):
            continue
        visited[row][col]=1
        dfs(row+1)
        visited[row][col]=0


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    answer=0
    visited=[[0]*N for _ in range(N)]
    dfs(0)
    print(f'#{tc} {answer}')