def recur(idx, s):
    global min_diff

    if s >= H: # 이미 s가 된 경우
        diff = s - H
        if diff < min_diff:
            min_diff = diff
        return

    if idx == N:  # 모든 원소 처리한 경우
        return

    recur(idx + 1, s + heights[idx])  # 현재 idx를 포함한 다음 idx 경우 재귀
    recur(idx + 1, s) # 현재 idx를 포함하지 않은 다음 idx 경우 재귀


T = int(input())

for tc in range(1,T+1):
    N,H = map(int,input().split())
    heights = list(map(int, input().split()))

    heights.sort(reverse=True)

    min_diff = sum(heights)

    recur(0,0)

    print(f'#{tc} {min_diff}')