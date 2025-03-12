def eat(arr):    # 배열을 거꾸로 뒤집어서, 각 상자의 사탕 개수가 순감소하도록 만들어보자.
    arr[0], arr[2] = arr[2], arr[0]

    cnt = 0    # 사탕 먹은 횟수
    for i in range(2):
        while arr[i] <= arr[i+1]:    # 현재 상자와 다음 상자의 사탕 수가 같거나 더 많으면 
            arr[i+1] -= 1    # 다음 상자의 사탕을 먹는다.
            cnt += 1
            if arr[i+1] < 1:    # 상자의 사탕이 1개 미만으로 떨어지면 실패!
                return -1
    return cnt


T = int(input())
for tc in range(1, T+1):
    candy = list(map(int, input().split()))
    result = eat(candy)
    print(f"#{tc} {result}")
