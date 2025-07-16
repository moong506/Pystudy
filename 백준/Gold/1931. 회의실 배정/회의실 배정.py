import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([end, start])
arr.sort()

count, standard = 0, -1
for end, start in arr:
    if start >= standard:  # 회의실 예약 가능한 경우
        standard = end
        count += 1


print(count)