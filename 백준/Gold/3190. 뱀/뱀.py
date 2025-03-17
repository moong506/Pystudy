from collections import deque

change = {
    (0,1): ((1,0), (-1,0)),
    (1,0): ((0,-1), (0,1)),
    (0,-1): ((-1,0), (1,0)),
    (-1,0): ((0,1), (0,-1))

}

N = int(input())  # 보드의 크기 N
K = int(input())  # 사과의 개수 K
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
turn = [input().split() for _ in range(L)]
for i in range(len(turn)-1, 0, -1):
    turn[i][0] = int(turn[i][0]) - int(turn[i-1][0])
turn[0][0] = int(turn[0][0])
turn.append([100, 0])
# apple 리스트를 만들어보자
apple_lst = [[0] * N for _ in range(N)]
for i, j in apple:
    apple_lst[i-1][j-1] = 1
q = deque([(0, 0)])
di, dj = 0, 1
cnt = 0
result = True
visited = deque([(0, 0)])
while True:
    if not q:
        break
    i, j = q.popleft()
    a, b = turn.pop(0)
    for k in range(1, a + 1):
        ni, nj = i + di*k, j + dj*k
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
            if apple_lst[ni][nj] == 1:
                apple_lst[ni][nj] = 0  # 사과를 먹었으므로 제거
            else:
                visited.popleft()  # 꼬리 제거
            visited.append((ni, nj))
            cnt += 1
        else:
            result = False
            break
    if not result:
        break
    q.append((ni, nj))
    if b == 'L':
        di, dj = change[(di, dj)][1]
    elif b == 'D':
        di, dj = change[(di, dj)][0]

print(cnt+1)