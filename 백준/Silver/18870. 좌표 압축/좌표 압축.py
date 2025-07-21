import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
# 1. 중복 없이 각 숫자 넣기
new_set = list(set(arr))
new_set.sort()
new_dict = {}

# 2. 작은 수부터 정렬해서 딕셔너리에 입력
for i in range(len(new_set)):
    new_dict[new_set[i]] = i

new_arr = [0]*N
# 3. O(n)으로 끝내보자!!
for i in range(N):
    new_arr[i] = new_dict[arr[i]]
print(*new_arr)

