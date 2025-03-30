import sys

def find_set(x): # 대표자 찾기
    if x == parents[x]: # 자기 자신이 대표자라면
        return x # 자기 자신 반환
    # else:
    parents[x] = find_set(parents[x]) # x의 대표자를 x의 최종 대표자(최소 조부모)로 변경 (압축)
    return parents[x] # x의 대표자를 반환

def union_set(x,y): # x와 y를 같은 그룹에 넣기
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y: # 둘의 대표자가 이미 같음
        return
    # else: 
    if ref_x > ref_y: # 더 작은 숫자를 대표자로 설정할거라 ref_y가 더 작은 경우
        parents[ref_x] = ref_y # ref_x의 대표자를 변경
    else:
        parents[ref_y] = ref_x


N = int(input())
M = int(input())

edges = []
parents = [i for i in range(N+1)]

for _ in range(M):
    s, g, w = map(int, input().split())

    edges.append((s, g, w))

# 모든 컴퓨터를 연결할 수 있다 했기 때문에 제일 싼 순으로 다 연결될 때까지 고를 거임(최소비용)
edges.sort(key=lambda x:x[2]) # 싼 순으로 정렬

total = 0

for s, g, w in edges:
    if find_set(s) != find_set(g): # 같은 그룹이 아니면
        union_set(s,g) # 합치기
        total += w # 연결했으니까 비용에 추가

print(total)