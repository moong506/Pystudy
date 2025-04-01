def combinations(arr, r):
    result = []
    path = []  # 현재 선택된 원소들을 저장할 리스트

    # 조합
    def recur(cnt, start):
        if cnt == r:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            recur(cnt + 1, i + 1)
            path.pop()

    recur(0, 0)
    return result


# 치킨 거리 계산
def chick_dist(house, chicken_shop):
    return abs(house[0] - chicken_shop[0]) + abs(house[1] - chicken_shop[1])


# 도시의 치킨 거리 계산
def city_dist(remain):
    total_distance = 0
    for house in houses:
        # 각 집에서 가장 가까운 치킨집까지의 거리 계산
        min_distance = float('inf')
        for shop in remain:
            distance = chick_dist(house, shop)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance


N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

# 집과 치킨집 위치 찾기
houses = []
chicken_shops = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:  # 집
            houses.append((i, j))
        elif city[i][j] == 2:  # 치킨집
            chicken_shops.append((i, j))


# M개의 치킨집을 선택하는 모든 조합에 대해 도시의 치킨 거리 계산
min_city_distance = float('inf')
for selected_shops in combinations(chicken_shops, M):
    city_distance = city_dist(selected_shops)
    min_city_distance = min(min_city_distance, city_distance)

# 결과 출력
print(min_city_distance)