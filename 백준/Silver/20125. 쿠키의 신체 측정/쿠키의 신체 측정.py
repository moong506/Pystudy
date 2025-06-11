N = int(input())
arr = [list(input()) for _ in range(N)]

# 심장 초기 인덱스 (근데 여기에 선언을 꼭 해야하는지는 모르겠음!
heart_i, heart_j = 0, 0

# 심장 위치 찾기
flag = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '*':
            heart_i, heart_j = i+1, j
            flag = 1
            print(heart_i+1, heart_j+1)
            break
    if flag == 1:
        break
# 각각 값을 담을 것임!
ans = [1, 1, 1, 1, 1]

arm = arr[heart_i]  # 뭔가 1차원 배열을 담은 변수를 탐색하는 게 시간이 덜 걸릴 것 같아서 따로 빼봤습니다.

# 1. 왼쪽 팔부터 찾아봅시다!
left = 0
while True:
    if arm[left] == '*':
        break
    left += 1

# 왼쪽 팔 정답 저장
ans[0] = heart_j - left


# 2. 오른쪽 팔 찾기
right = N-1
while True:
    if arm[right] == '*':
        break
    right -= 1

# 오른쪽 팔 정답 저장
ans[1] = right - heart_j


# 3. 몸통 찾기
body = N-1
while True:
    if arr[body][heart_j] == '*':
        break
    body -= 1

# 몸통 정답 저장
ans[2] = body - heart_i


# 4. 왼쪽 다리 찾기
left_leg = N-1
while True:
    if arr[left_leg][heart_j-1] == '*':
        break
    left_leg -= 1

# 왼쪽 다리 정답 저장
ans[3] = left_leg - body

# 5. 오른쪽 다리 찾기
right_leg = N-1
while True:
    if arr[right_leg][heart_j+1] == '*':
        break
    right_leg -= 1

# 오른쪽 다리 정답 저장
ans[4] = right_leg - body

print(*ans)