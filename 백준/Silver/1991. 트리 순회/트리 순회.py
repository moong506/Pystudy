def preorder(root):
    if root != '.':
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


N = int(input())
tree = {}  # 딕셔너리 사용

for i in range(1, N+1):
    root, left_c, right_c = input().split()
    tree[root] = [left_c, right_c]  # 딕셔너리에 노드 정보 저장

preorder('A')  # 전위 순회
print()
inorder('A')  # 중위 순회
print()
postorder('A')  # 후위 순회



