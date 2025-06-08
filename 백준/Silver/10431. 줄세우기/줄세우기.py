N = int(input())
for _ in range(N):
    tc, *arr = input().split()
    arr = list(map(int, arr))
    count = 0
    max_idx = 0
    for i in range(1, 20):
        if arr[max_idx] < arr[i]:
            max_idx = i
        else:
            for j in range(i):
                if arr[j] > arr[i]:
                    max_idx += 1
                    arr.insert(j, arr.pop(i))
                    count += i-j
                    break

    print(tc, count)
