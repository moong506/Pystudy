N = int(input())
arr = list(map(int, input().split()))
nge = [-1] * N   # 오큰수 수열
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]: # stack이 차있고, top의 요소가 arr[i]보다 작을 때
        idx = stack.pop()
        nge[idx] = arr[i] # 해당 수의 오큰수는 arr[i]
    stack.append(i)

print(*nge)