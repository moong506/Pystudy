T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    while True:  
        max_value = max(arr)  # 최대값 저장
        last_max_index = max(i for i, v in enumerate(arr) if v == max_value)  # 최대 값의 인덱스 저장
        i = 0
        while i < last_max_index:  # 최대 값 전까지는 다 사고 최대 값에서 팔기
            ans += arr[last_max_index] - arr[i]
            i += 1
        arr = arr[last_max_index+1:]  # 그 다음부터 다시 찾아보기
        if arr == []:  # 다 찾았으면 break 하기
            break
    print(f'#{tc} {ans}')