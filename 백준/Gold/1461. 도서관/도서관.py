N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst1 = []  # 음수 담기
lst2 = []  # 양수 담기
max_idx = 0
count = 0
for i in range(N):
    if arr[i] > 0:
        lst2.append(arr[i])
    else:
        lst1.append(arr[i])

if lst1 != [] and lst2 != []:
    if abs(lst1[0]) > lst2[-1]:  # 제일 먼 거리가 음수인 경우
        max_idx = 1
    else:  # 제일 먼 거리가 양수인 경우
        max_idx = 2

for i in range(0, len(lst1), M):
    if max_idx == 1 or max_idx == 0:  # 제일 먼 거리가 음수인 경우 or lst1만 함수가 있는 경우
        max_idx = -1
        count += abs(lst1[i])
    else:
        count += abs(lst1[i])*2

for i in range(len(lst2) - 1, -1, -M):
    if max_idx == 2 or max_idx == 0:  # 제일 먼 거리가 양수인 경우 or lst2만 함수가 있는 경우
        max_idx = -1
        count += lst2[i]
    else:
        count += lst2[i]*2
print(count)