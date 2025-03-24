import sys

def make_sum_matrix():
    global sum_arr
    for i in range(1,N-1):
        for j in range(1,N-1):
            sum_arr[i][j] = arr[i][j]
            for x in range(4):
                sum_arr[i][j] += arr[i+di[x]][j+dj[x]]

def find_min_sum(total,cnt,visited):
    global min_total
    if cnt == 3:
        min_total = min(min_total,total)
        return

    if total>min_total:
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if visited[i][j] == 0 and visited[i][j+1] == 0 and visited[i+1][j]==0 and visited[i][j-1]==0 and visited[i-1][j]==0:
                visited[i][j] = visited[i][j+1] = visited[i+1][j] = visited[i][j-1]= visited[i-1][j] = 1
                find_min_sum(total + sum_arr[i][j], cnt + 1, visited)
                visited[i][j] = visited[i][j+1] = visited[i+1][j] = visited[i][j-1]= visited[i-1][j] = 0

N = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
min_total = 3000 # 200 * 5 * 3

di = [0,1,0,-1]
dj = [1,0,-1,0]

mi = [0,2,0,-2,1,-1,1,-1]
mj = [2,0,-2,0,1,-1,-1,1]

make_sum_matrix()
find_min_sum(0,0,visited)
print(min_total)
