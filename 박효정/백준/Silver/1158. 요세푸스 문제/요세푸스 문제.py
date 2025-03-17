# 아마도 원형큐?
# 요세푸스 문제
N, K = map(int, input().split()) # 7, 3
q = [i for i in range(1, N+1)]
front = 0
result = []

while q:
    front = (front + K -1) % len(q) # 현재 큐 길이로 나눠야 하는구나..............
    result.append(q.pop(front))

print('<', ', '.join(map(str, result)), '>', sep='')