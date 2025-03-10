T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = arr[::-1]
    profit = 0
    fv = arr[0]

    for i in range(1, N):
        if fv > arr[i]:
            profit += fv-arr[i]
        else:
            fv = arr[i]

    print(f'#{tc} {profit}')