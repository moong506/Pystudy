# ATM
# 최솟값의 경우, 시간이 짧은 순서대로 먼저 줄을 서야한다.
T=int(input())
arr=list(map(int,input().split()))

arr.sort()
total=0

# T가 5이면, 맨 앞 숫자는 5번, 그 다음 숫자는 4번 더해진다.
for i in range(T):
    total+=(arr[i]*(T-i))
print(total)