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

# 포화 이진 트리가 아닐 때 root 찾기
# # 층마다 몇 개씩인지 세기
# N = len(in_order)
# M = N
# H = [] # 층마다 몇 개씩 있는지
# for i in range(K):
#     n = 2**i
#     if n>M:
#         H.append(M)
#         break
#     H.append(n)
#     M -= n
#
# root = 1
# for j in range(K-1, 0, -1):
#     left = (2**j)//2
#     if H[j]<left:
#         root += H[j]
#     else:
#         root += left
