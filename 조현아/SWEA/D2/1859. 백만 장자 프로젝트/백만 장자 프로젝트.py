T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    profit = 0
    max_idx = 0
    start_idx = 0

    while start_idx < N:
        # 현재 구간에서 가장 높은 가격 찾기
        max_price = 0
        max_idx = start_idx

        for i in range(start_idx, N):
            if price[i] > max_price:
                max_price = price[i]
                max_idx = i

        # 시작점부터 최대값 전까지 이익 계산
        for i in range(start_idx, max_idx):
            profit += max_price - price[i]

        # 다음 구간의 시작점 설정
        start_idx = max_idx + 1

    print(f'#{tc} {profit}')