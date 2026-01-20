import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 첫번째 값과 마지막 값 중 큰 값으로 설정
ans = max(sum(arr[:K]), sum(arr[N-K:]))
com = sum(arr[:K])
com_i = 0


for i in range(1,N-K):
    target = com - arr[com_i] + arr[i+K-1]
    if ans < target:
        ans = target
    com = target
    com_i += 1


print(ans)

