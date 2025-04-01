N = int(input())
nums = list(map(int,input().split()))
cnt = 0

for num in nums:
    i = 2
    while num>=i:

        if i == num:
            cnt += 1
            break
        elif num%i==0:
            break
        else:
            i += 1

print(cnt)