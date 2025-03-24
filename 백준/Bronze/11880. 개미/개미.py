T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    ans = (arr[0] + arr[1])**2 + arr[2]**2
    print(ans)