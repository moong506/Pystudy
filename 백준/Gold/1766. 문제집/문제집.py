import heapq
def sort_num():
    pq = []
    for i in range(1, N+1):
        if init_arr[i] == 0:
            pq.append(i)
    ans = []
    while pq:
        num = heapq.heappop(pq)
        ans.append(num)
        for next_num in arr[num]:
            init_arr[next_num] -= 1
            if init_arr[next_num] == 0:
                heapq.heappush(pq, next_num)

    return ans





N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
init_arr = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    init_arr[B] += 1

answer = sort_num()
print(*answer)


