# 7, 6
# 11
C, R = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]
arr[R-1][0] = 1
direction = [[-1,0], [0,1], [1,0], [0,-1]]
direction_idx = 0
q = [(R-1,0)]
ans_x = -1
ans_y = -1
while q:
    ti, tj = q.pop(0)
    if arr[ti][tj] == K:
        ans_x = ti
        ans_y = tj
        break
    if arr[ti][tj] == R*C:
        break
    ni, nj = ti+direction[direction_idx][0], tj+direction[direction_idx][1]
    if 0<=ni<R and 0<=nj<C and arr[ni][nj] == 0:
        arr[ni][nj] = arr[ti][tj] + 1
        q.append((ni,nj))
    else:
        direction_idx += 1
        direction_idx %= 4
        q.append((ti,tj))
if ans_x == -1:
    print(0)
else:
    print(ans_y+1, R-ans_x)
