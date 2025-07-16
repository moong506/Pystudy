import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()  # 오름차순 정렬

M = int(input())
test = list(map(int, input().split()))
for num in test:
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == num:
            print(1)
            break
        elif A[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(0)