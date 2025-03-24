N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 1000001
stack = []
ngf = [-1] * N

for num in arr:
    cnt[num] += 1

for i in range(N):
    while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
        idx = stack.pop()
        ngf[idx] = arr[i]
    stack.append(i)

print(*ngf)