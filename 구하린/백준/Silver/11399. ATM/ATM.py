N = int(input())

arr = list(map(int,input().split()))
arr.sort() # 작은 순서대로 정렬하고 앞에서부터 피보나치 해줄 겁니다

total = arr[0]

for i in range(1,N):
    arr[i] += arr[i-1]
    total += arr[i]

print(total)