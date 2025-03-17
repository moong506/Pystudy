# T = int(input())

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    for i in range(2, N-2):
        neighbor_lst = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]

        if arr[i] > max(neighbor_lst):
            cnt += arr[i]-max(neighbor_lst)

    print(f'#{tc} {cnt}')
