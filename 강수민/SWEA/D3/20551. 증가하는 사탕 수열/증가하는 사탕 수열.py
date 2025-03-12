T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    candy = 0

    while True:
        if A < B < C:
            break

        if B >= C:
            B -= 1
            candy += 1
        if A >= B:
            A -= 1
            candy += 1
        if A == 0 or B == 0:
            candy = -1
            break

    print(f'#{tc} {candy}')