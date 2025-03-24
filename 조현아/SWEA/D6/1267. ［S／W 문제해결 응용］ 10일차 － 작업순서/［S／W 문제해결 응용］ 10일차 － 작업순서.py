from collections import deque

def tp_sort(V):
    global ans
    q=deque()       # 큐 생성
    for i in range(1,V+1):  # 집인차수가 0인 정점 인큐
        if ind[i]==0: # 진입차수가 0인 노드부터 먼저 큐에 인큐해서 처리한다.
            q.append(i)
    while q:
        t=q.popleft() # 하나씩 빼서 처리하고,
        ans.append(t)
        # t에 인접한 i의 진입 차수 1 감소
        for w in adj_l[t]:
            ind[w]-=1
            if ind[w]==0: # 모든 선행작업이 완료된 경우 이므로
                q.append(w)


T=10
for tc in range(1,T+1):
    V,E=map(int,input().split())
    arr=list(map(int,input().split()))

    adj_l=[[] for _ in range(V+1)]
    ind=[0]*(V+1)
    for i in range(E):
        num_1=arr[2*i]
        num_2=arr[2*i+1]
        adj_l[num_1].append(num_2) # 출발 정점을 인덱스로 도착간선 저장
        ind[num_2]+=1 # 진입차수는 도착으로 언급된 횟수


    ans=[]
    tp_sort(V)
    print(f'#{tc}', *ans)