# Baekjoon 9934 완전 이진 트리 (2025.03.09)

# import sys

# 중위 순회로 완전 이진 트리 순서대로 값 채우기
def complete_tree(arr, city, idx, start, end):
    """
    :param arr: input으로 받은 노드의 값들
    :param city: 중위 순회로 순서대로 값이 채워진 완전 이진 트리 배열
    :param idx: 현재 노드의 인덱스 값
    :param start: 시작 인덱스
    :param end: 끝 인덱스
    :return: 없음
    """
    # 종료 조건
    if start > end:
        return
    # 중간 값 구하기
    mid = (start + end) // 2
    # 빈 노드의 값 채워주기
    city[idx] = arr[mid]
    # 왼쪽 자식에 적용
    complete_tree(arr, city, 2 * idx, start, mid - 1)
    # 오른쪽 자식에 적용
    complete_tree(arr, city, 2*idx + 1, mid + 1, end)

# sys.stdin = open("9934_input.txt", "r")
# sys.stdout = open("9934_my_output.txt", "w")

K = int(input())
arr = list(map(int, input().split()))
city = [None] * (2 ** K)
complete_tree(arr, city, 1, 0, len(arr) - 1)
for i in range(K):
    for j in range(2 ** i, 2 ** (i + 1)):
        print(city[j], end=" ")
    print()
