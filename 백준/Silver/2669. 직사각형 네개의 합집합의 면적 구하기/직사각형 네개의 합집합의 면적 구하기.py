rec1_x1, rec1_y1, rec1_x2, rec1_y2 = map(int, input().split())
rec2_x1, rec2_y1, rec2_x2, rec2_y2 = map(int, input().split())
rec3_x1, rec3_y1, rec3_x2, rec3_y2 = map(int, input().split())
rec4_x1, rec4_y1, rec4_x2, rec4_y2 = map(int, input().split())
arr = [[0]*100 for _ in range(100)]
# i,j range는 직접 수기로 그려보면서 설정했음
# row에 영향을 미치는 값은 y
    # 그 중에서도 오른쪽 위 좌표(y2)가 row의 시작에 관여
# col에 영향을 미치는 값은 x
    # 그 중에서도 왼쪽 아래 좌표 (x1)가 col의 시작에 관여
for i in range(100-rec1_y2+1, 100-rec1_y1+1):
    for j in range(rec1_x1, rec1_x2):
        arr[i][j] = 1
for i in range(100-rec2_y2+1, 100-rec2_y1+1):
    for j in range(rec2_x1, rec2_x2):
        arr[i][j] = 1
for i in range(100-rec3_y2+1, 100-rec3_y1+1):
    for j in range(rec3_x1, rec3_x2):
        arr[i][j] = 1
for i in range(100-rec4_y2+1, 100-rec4_y1+1):
    for j in range(rec4_x1, rec4_x2):
        arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)