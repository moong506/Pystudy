# 완전 이진 트리
N = int(input())
arr = list(map(int, input().split()))
# 중위순회(LVR)
result = [[] for _ in range(N)]  # 결과값을 저장할 리스트

# 재귀 함수로 트리 구성
def build_tree(start, end, depth):
    if start > end:
        return

    mid = (start + end) // 2
    result[depth].append(arr[mid])

    build_tree(start, mid - 1, depth + 1)  # 왼쪽 서브트리
    build_tree(mid + 1, end, depth + 1)  # 오른쪽 서브트리


# 트리 구성 시작
build_tree(0, len(arr) - 1, 0)

# 결과 출력
for j in range(len(result)):
    print(*result[j])