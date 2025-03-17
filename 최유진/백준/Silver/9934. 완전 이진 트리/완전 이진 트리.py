def r_inorder(start, end, level):
    if start > end:
        return
    mid = (start + end) // 2
    ans[level].append(tree[mid])
    r_inorder(start, mid - 1, level + 1)
    r_inorder(mid + 1, end, level + 1)

K = int(input())               # 트리의 깊이
N = 2**K - 1                   # 노드 수
tree = list(map(int, input().split()))
ans = [[] for _ in range(K)]   # 각 레벨의 노드를 저장할 리스트

r_inorder(0, N - 1, 0)

for level in ans:
    print(" ".join(map(str, level)))
