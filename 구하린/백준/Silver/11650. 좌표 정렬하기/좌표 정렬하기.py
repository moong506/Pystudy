N=int(input())
arr = []
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort()

for x in arr:
    print(*x)