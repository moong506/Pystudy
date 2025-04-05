T = int(input())
for tc in range(T):
    n = int(input())
    arr = [0] * (n+1)
    arr[1] = 1
    if n == 1:
        print(1)
        continue
    arr[2] = 2
    if n == 2:
        print(2)
        continue
    arr[3] = 4
    for i in range(4, n+1):
        arr[i] = (arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009
    print(arr[n])
