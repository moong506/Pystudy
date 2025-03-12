def previous_permutation(arr):
    i = N - 1
    # 뒤에서부터 첫 번째로 오름차순이 아닌 위치 찾기
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    # 이미 가장 작은 순열이면 이전 순열이 없음
    if i <= 0:
        return False

    j = N - 1
    # arr[i-1]보다 작은 값 중 가장 오른쪽에 있는 원소 찾기
    while arr[j] >= arr[i - 1]:
        j -= 1

    # arr[i-1]과 arr[j] 교환
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # arr[i:]를 역순 정렬하여 이전 순열 완성 ([1,5,2,3,4] 인 경우 [1,4,5,3,2]가 이전 순열이라 그냥 교환만 하면 [1,4,2,3,5]라 안 맞음)
    arr[i:] = arr[N - 1 : i - 1 : -1]
    # range(N-1,i-1,-1)느낌 => arr[N-1:i]까지 뒤집어라
    # 근데[:i]면 실제러는 arr[i+1]번까지라서 arr[i+1:]을 뒤집는거
    # arr[i:] = arr[:i+1] + arr[i+1:N:-1]

    return True

N = int(input())
arr = list(map(int, input().split()))
if not previous_permutation(arr): # False면(이전 인덱스 없으면)
    print(-1)
else: # True면 정리한 arr 출력
    print(*arr)
