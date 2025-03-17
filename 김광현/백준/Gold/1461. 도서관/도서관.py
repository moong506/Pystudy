N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 절대값 기준으로 정렬 (가장 먼 곳이 마지막)
arr.sort()

# 음수, 양수를 분리하여 가장 먼 거리를 찾음
arr_minus = [x for x in arr if x < 0]  # 왼쪽 방향
arr_plus = [x for x in arr if x > 0]   # 오른쪽 방향

max_distance = max(abs(arr[0]), abs(arr[-1]))  # 가장 먼 거리

result = 0

# 왼쪽(음수) 방향 처리
for i in range(0, len(arr_minus), M):
    result += 2 * abs(arr_minus[i])

# 오른쪽(양수) 방향 처리
for i in range(len(arr_plus) - 1, -1, -M):
    result += 2 * arr_plus[i]

# 가장 먼 거리는 한 번만 이동하도록 조정
print(result - max_distance)