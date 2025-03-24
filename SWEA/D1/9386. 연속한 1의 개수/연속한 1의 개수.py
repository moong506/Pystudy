T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    # print(arr)
    cnt = 0
    max_cnt = 0
    for i in range(N):
        if arr[i] == '1':
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 0

    print(f'#{tc} {max(cnt, max_cnt)}')