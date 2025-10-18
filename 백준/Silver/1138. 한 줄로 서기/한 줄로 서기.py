N = int(input())
arr = list(map(int, input().split()))
answer = [0]*N

for i in range(N):
    cnt = 0
    j = 0
    while cnt < arr[i]:
        if answer[j] == 0:
            cnt += 1
        j += 1
    for k in range(j,N):
        if answer[k] == 0:
            answer[k] = i+1
            break

print(*answer)