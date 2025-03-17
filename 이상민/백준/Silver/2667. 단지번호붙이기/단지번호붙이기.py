n = int(input())
village = [list(map(int, list(input()))) for _ in range(n)]

queue = [0] * (n ** 2)
visit = [[0] * n for _ in range(n)]
danji = []

for i in range(n):
    for j in range(n):
        if village[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            front = rear = -1
            rear += 1
            queue[rear] = [i, j]
            house = 1
            while front != rear:
                front += 1
                y, x = queue[front]
                for dy, dx in [[1,0], [0,1], [-1,0], [0,-1]]:
                    ny = y + dy
                    nx = x + dx
                    if 0<=ny<n and 0<=nx<n and village[ny][nx] == 1 and visit[ny][nx] == 0:
                        rear += 1
                        queue[rear] = [ny, nx]
                        visit[ny][nx] = 1
                        house += 1
            danji.append(house)

danji.sort()
print(len(danji))
for i in danji:
    print(i)
