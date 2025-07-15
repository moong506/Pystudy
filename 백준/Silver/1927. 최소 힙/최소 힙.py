import heapq
import sys
N = int(sys.stdin.readline())
lst = []
heapq.heapify(lst)
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if lst:
            print(heapq.heappop(lst))
        else:
            print(0)
    else:
        heapq.heappush(lst, x)
    