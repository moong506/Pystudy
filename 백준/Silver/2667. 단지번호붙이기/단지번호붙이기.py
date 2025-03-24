dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(i, j):
    global cnt
    n = len(arr)

    if 0 <= i < n and 0 <= j < n and arr[i][j] == 1:
        arr[i][j] = 0
        cnt += 1

        for x in range(4):
            ni = i + dx[x]
            nj = j + dy[x]
            dfs(ni, nj)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
total_cnt = 0
total_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j)
            total_list.append(cnt)
            total_cnt += 1
            cnt = 0

print(total_cnt)

total_list.sort()
for i in range(total_cnt):
    print(total_list[i])