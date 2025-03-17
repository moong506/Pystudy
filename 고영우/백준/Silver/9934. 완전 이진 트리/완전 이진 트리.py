def binary(arr, level, start, end, levels):
    if start<= end:
        mid = (start+end)//2
        levels[level].append(arr[mid])
        binary(arr,level+1, start, mid-1, levels)   # 왼쪽 서브트리
        binary(arr,level+1, mid+1, end, levels) # 오른쪽 서브트리

K = int(input())
arr = input().split()
levels = [[] for _ in range(K)]
binary(arr, 0, 0, len(arr)-1, levels)
mid_idx = len(arr)//2
mid = arr[mid_idx]
for level in levels:
    print(*level)