# 트리순회
# 수업시간에서와 달리, 문자열로 트리가 구성되어 있어서, 리스트가 아닌 딕셔너리로 접근해야 했음.
def pre_order(T):
    if T!='.': # 존재하는 정점이면,
        print(T, end='') # V
        pre_order(left.get(T,'.')) # L (키가 T인 값을 가져와라. 만약 없으면 .을 가져와라)
        pre_order(right.get(T,'.')) # R

def in_order(T):
    if T!='.': # 존재하는 정점이면,
        in_order(left.get(T,'.')) # L
        print(T, end='') # V
        in_order(right.get(T,'.')) # R

def post_order(T):
    if T!='.': # 존재하는 정점이면,
        post_order(left.get(T,'.')) # L
        post_order(right.get(T,'.')) # R
        print(T, end='') # V


N=int(input())
arr=[input().split() for _ in range(N)]
E=N-1 # 간선의 수는 (노드의 수 -1)

# 딕셔너리로 구성 
left = {}
right = {}

# 간선에 대한 정보 저장.
for i in range(N):
    parent=arr[i][0]
    if arr[i][1]!='.':
        left[parent]=arr[i][1]
    else:
        left[parent]='.'
    if arr[i][2]!='.':
        right[parent]=arr[i][2]
    else:
        right[parent]='.'

pre_order('A')
print()
in_order('A')
print()
post_order('A')