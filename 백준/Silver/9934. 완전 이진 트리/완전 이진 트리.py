# 중위 순회의 순서가 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램
# 완전 이진 트리니까 층별로 맨 오른쪽부터 줄바꾸면서 구해라
import sys

def find_depth(arr, depth):
    if not len(arr):
        return

    parent = len(arr)//2
    complete_binary_tree[depth].append(arr[parent])

    find_depth(arr[:parent], depth+1) # parent 기준 왼쪽
    find_depth(arr[parent + 1:], depth+1) # parent 기준 오른쪽

K = int(sys.stdin.readline()) # 깊이
in_order = list(map(int, sys.stdin.readline().split()))

complete_binary_tree = [[] for _ in range(K)]
find_depth(in_order, 0)

for floor in complete_binary_tree:
    print(*floor)