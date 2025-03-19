def can_place(x,y):
    if visited[x][y]!=0:
        return False
    for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni,nj=x+di,y+dj
        # 방문한 적이 없고, 범위 내에 있으면
        if not 0<=ni<N or not 0<=nj<N or not visited[ni][nj]==0:
            return False
    return True

def flower(cost,num):
    global min_cost
    # 가지치기
    if cost>min_cost:
        return

    if num==3:
        if min_cost > cost:
            min_cost = cost
        return

    for i in range(N):
        for j in range(N):
            if can_place(i,j): # 해당 위치에 씨앗을 심을 수 있는 경우
                visited[i][j],visited[i+1][j],visited[i-1][j],visited[i][j+1],visited[i][j-1]=1,1,1,1,1
                flower_cost=(arr[i][j]+arr[i+1][j]+arr[i-1][j]+arr[i][j+1]+arr[i][j-1])
                flower(cost+flower_cost,num+1)

                # 다시 원상복귀
                visited[i][j]=0
                visited[i][j], visited[i + 1][j], visited[i - 1][j], visited[i][j + 1], visited[i][
                    j - 1] = 0,0,0,0,0



N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
cnt=0
min_cost=10**9
flower(0,0)
print(min_cost)