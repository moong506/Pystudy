T = int(input())

for tc in range(1, T+1):
    arr = input().split()
    for a in arr:
        print(a[::-1], end=" ")
    print()