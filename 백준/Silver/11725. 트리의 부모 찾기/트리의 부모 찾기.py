import sys
input = sys.stdin.readline

N = int(input())      # 노드 개수
par = [0] * (N+1)  # 부모 저장 배열(인덱스가 자식)
adj_lst = [[] for _ in range(N+1)]  # 인접 리스트

for _ in range(N-1):    # 간선 만큼 입력 받기
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

s = [1]         # 루트에서 시작
par[1] = -1     # 루트의 부모는 없음
# 부모 찾아주기
while s:
    node = s.pop()
    for ch in adj_lst[node]:
        if par[ch] == 0:    # 방문x 경우 처리
            par[ch] = node  # 부모 저장
            s.append(ch)    # 스택 추가

# 2번 노드부터 순서대로 출력
for i in range(2, N+1):
    print(par[i])