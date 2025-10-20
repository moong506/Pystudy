import math
N = int(input())
count = 0
ans = 0
for i in range(N):
    if (i*1 + (N-i)*5) % 3 == 0:
        a = math.factorial(N-1)
        b = math.factorial(i)
        c = math.factorial(N-1-i)
        count += a//(b*c)
        ans = count % 1000000007
print(ans)