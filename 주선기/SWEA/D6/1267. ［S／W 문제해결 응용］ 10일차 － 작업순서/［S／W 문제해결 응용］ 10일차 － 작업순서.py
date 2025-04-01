from collections import deque
 
def tp_sort(V):
    # 큐 생성
    dq = deque()
    # 진입 차수가 0인 정점 인큐
    for i in range(1, V + 1):
        if ind[i] == 0:
            dq.append(i)
    while dq:
        t = dq.popleft()
        ans.append(t)
        # t에 인접한 i의 진입 차수 1 감소
        for w in adj_list[t]:
            ind[w] -= 1
            # 모든 선행 작업이 완료된 경우이므로
            if ind[w] == 0:
                dq.append(w)
 
for tc in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    # 인접 리스트
    adj_list = [[] for _ in range(V + 1)]
    # 진입 차수
    ind = [0] * (V + 1)
    for i in range(E):
        n1, n2 = arr[i * 2], arr[i*2 + 1]
        adj_list[n1].append(n2)
        # 진입차수는 도착으로 언급된 횟수
        ind[n2] += 1
    ans = []
    tp_sort(V)
    print(f"#{tc}", *ans)