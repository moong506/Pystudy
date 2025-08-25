N,M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
min_v = 64
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for k in range(8):
            for m in range(8):
                if k % 2 == 0 and m % 2 == 0:
                    if chess[i+k][j+m] == 'B':
                        count += 1
                elif k % 2 == 1 and m % 2 == 1:
                    if chess[i+k][j+m] == 'B':
                        count += 1
                else:
                    if chess[i+k][j+m] == 'W':
                        count += 1
        if count > 32:
            count = 64-count
        if min_v > count:
            min_v = count

print(min_v)

