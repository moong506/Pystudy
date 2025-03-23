# 최소비용 구하기
# 시작점부터 도착지점까지 가는데 드는 최소 비용을 구하는 문제이므로 다익스트라 적용

def dijkstra(start_node):
    INF=int(21e8)
    pq=[(0,start_node)] # 누적 금액, 도시 번호
    price=[INF]*(N+1) # 각 도시까지의 최대 금액으로 초기화
    price[start_node]=0 # 첫 도시에서의 금액은 0

    while pq:
        money,node=heapq.heappop(pq)

        if price[node]<money: # 이미 더 작은 금액으로 온 적이 있으면 건너뛰기
            continue
        for next_city in graph[node]:
            next_price=next_city[0] # 다음 도시로 가기 위한 금액
            next_node=next_city[1] # 다음 도시

            new_price=money+next_price

            if price[next_node]<=new_price:# 이미 더 작은 금액으로 온 적이 있으면 건너뛰기
                continue

            price[next_node]=new_price
            heapq.heappush(pq,(new_price,next_node))
    return price



import heapq
N=int(input()) # 도시의 개수
M=int(input()) # 버스의 개수
arr=[list(map(int,input().split())) for _ in range(M)]
graph=[[] for _ in range(N+1)]
for i in range(M):
    start=arr[i][0]
    end=arr[i][1]
    money=arr[i][2]
    graph[start].append((money,end))
start_node,end_node=map(int,input().split())
result=dijkstra(start_node)[end_node]
print(result)
