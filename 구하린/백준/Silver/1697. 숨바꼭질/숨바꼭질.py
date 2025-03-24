from collections import deque

cal = [(lambda x:x+1),(lambda x:x-1),(lambda x:x*2)]

def f():
    que = deque()
    que.append(N)
    distance[N] = 1

    while que:
        idx = que.popleft()

        if idx == K:
            return
        else:
            for i in range(3): # 세 가지 연산을 돌면서 que에 추가
                tmp = cal[i](idx)
                if 0 <= tmp <= 100000 and distance[tmp] == 0: # 범위 내이고 방문하지 않은 경우. 먼저 방문한 것이 최소 거리일 수 밖에 없음
                    que.append(tmp)
                    distance[tmp] = distance[idx] + 1

N,K = map(int,input().split())

# swap하고 x+1,x*2만 했더니 답이 틀려서 그냥 최대로
# 생각해보면 막 2배로 가다가 한칸 뒤로 가는게 가장 짧을 수도 있으니까
distance = [0] * (100001) # 항상 고정된 최대 범위로 설정

f()

print(distance[K]-1)