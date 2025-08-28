N = int(input())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num - 1, N, num):
            arr[i] = 1 - arr[i]
    else:
        num -= 1
        arr[num] = 1 - arr[num]
        left = num - 1
        right = num + 1
        while True:
            if left < 0 or right >= N:
                break
            if arr[left] != arr[right]:
                break
            arr[left] = 1 -arr[left]
            arr[right] = 1- arr[right]
            left -= 1
            right += 1
        
for i in range(0, N, 20):
    print(*arr[i:i+20])