# N 개의 카드 중 3장을 뽑아 M이하이면서 가까운 숫자를 만들어라
N, M = map(int, input().split())
arr = list(map(int,input().split()))
max_sum = 0 # 최대값

# # 삼중 for 문
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1, N):
#             s = arr[i] + arr[j] + arr[k]
#             if s > M:
#                 continue
#             elif max_sum <= s:
#                 max_sum = s
# print(max_sum)

# 순열로 풀기 (재귀)
path=[] # 뽑힌 카드 저장
used = [0]*N # 카드 사용 여부
def recur(cnt):
    global max_sum
    if cnt==3: # 3장 뽑으면 종료
        total = sum(path)
        if total <= M:    # 합 확인
            if max_sum < total:
                max_sum = total
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        path.append(arr[i])
        recur(cnt+1)
        path.pop()
        used[i] = 0
recur(0)
print(max_sum)