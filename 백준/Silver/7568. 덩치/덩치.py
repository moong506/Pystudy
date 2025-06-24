N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    target_x = arr[i][0]
    target_y = arr[i][1]
    count = 1
    for j in range(N):
        if i == j:
            continue
        if target_x < arr[j][0] and target_y < arr[j][1]:
            count += 1
    print(count, end=' ')

print()