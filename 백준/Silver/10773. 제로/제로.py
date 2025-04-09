K = int(input())
stack = []

for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
ans = 0
for num in stack:
    ans += num
print(ans)
