from collections import deque

def tp_sort(V):
    q = deque()         # 큐 생성
    for i in range(1, V+1):
        if ind[i] == 0:
            q.append(i)
    while q:
        t = q.popleft()
        ans.append(t)
        for w in adj_l[t]:      # t에 인접한 i의 진입차수 1 감소
            ind[w] -= 1
            if ind[w] == 0:
                q.append(w)

T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_l = [[] for _ in range(V+1)]        # 인접 리스트
    ind = [0] * (V+1)                       # 진입차수
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]
        adj_l[n1].append(n2)
        ind[n2] += 1                        # 진입차수는 도착 정점인 경우의 횟수

    ans = []
    tp_sort(V)
    print(f'#{tc}', *ans)