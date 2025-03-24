
# 중위순회
def in_order(T):
    global s

    if T and T <= N:
        in_order(left[T])
        tree[T] = arr[s] # 0부터 집어넣기
        s += 1 # 추가
        in_order(right[T])

K = int(input())
arr = list(map(int, input().split()))
N = 2**K -1
tree = [0] * (N+1)
left = [0] * (N+1)
right = [0] * (N+1)

# 좌, 우 인덱스 배치
for i in range(1, N//2+1):
    if i*2 <= N:
        left[i] = i*2
    if i*2+1 <= N:
        right[i] = i*2+1

s = 0
in_order(1)

for i in range(K): # 0, 1, 2
    for j in range(2**i):
        print(tree.pop(1), end= " ")
    print()