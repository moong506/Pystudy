T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = [0] * N    # n번째 전선의 시작지점을 n-1번째 인덱스에 저장
    end = [0] * N    # 전선 끝지점
    for i in range(N):
        start[i], end[i] = map(int, input().split())

    cross = 0    # 교차 횟수
    for i in range(N):
        chk_s, chk_e = start[i], end[i]    # 전선 하나 선택
        for j in range(N):    # 다른 전선들과 비교 / 아래 조건문에 = 이 없어서 같은 전선끼리 교차점을 셀 일은 없음.
            if chk_s < start[j] and chk_e > end[j]:    # 선택한 전선이 다른 전선의 시작보다 낮고, 끝보다 높으면 1번 교차
                cross += 1
            elif chk_s > start[j] and chk_e < end[j]:    # 선택한 전선이 다른 전선의 시작보다 높고, 끝보다 낮으면 1번 교차
                cross += 1
    print(f"#{tc} {cross//2}")    # a 전선을 고르고 b 전선과 비교, b 전선을 고르고 a 전선과 비교 중복해서 세기 때문에 2로 나눠줌
