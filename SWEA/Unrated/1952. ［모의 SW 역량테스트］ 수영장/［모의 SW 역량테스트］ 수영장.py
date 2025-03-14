def f(i, s):  # i월에 수영장을 다니는 방법을 결정, s는 이전까지의 비용
    global min_v
    if i > 12:  # 12월까지 다니는 비용이 다 결제된 경우
        if min_v > s:
            min_v = s
    elif min_v <= s:
        return
    else:
        f(i + 1, s + min(day * use[i], month))
        f(i + 3, s + month3)


T = int(input())
for tc in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    use = [0] + list(map(int, input().split()))  # 1월~12월 월별 이용일

    min_v = year  # 1년권 비용으로 초기화
    f(1, 0)
    print(f'#{tc} {min_v}')