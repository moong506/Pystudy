N = int(input())
arr = [input() for _ in range(N)]

# 가로 방향 탐색
w = 0  # 가로로 누을 수 있는 자리
i = 0
while i < N:
    cnt = 0  # 자리 카운트
    j = 0
    while j < N:
        if arr[i][j] == 'X':
            if cnt >= 2:
                w += 1
            cnt = 0
        else:  # arr[i][j] == '.'
            cnt += 1
            if j == N-1 and cnt >= 2:
                w += 1
        j += 1
    i += 1

# 세로 방향 탐색
h = 0  # 세로로 누울 수 있는 자리
j = 0
while j < N:
    cnt = 0  # 자리 카운트
    i = 0
    while i < N:
        if arr[i][j] == 'X':
            if cnt >= 2:
                h += 1
            cnt = 0
        else:  # arr[i][j] == '.'
            cnt += 1
            if i == N-1 and cnt >= 2:
                h += 1
        i += 1
    j += 1

print(w, h)