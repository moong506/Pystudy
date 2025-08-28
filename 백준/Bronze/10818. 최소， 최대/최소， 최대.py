N = int(input())
arr = list(map(int, input().split()))

max_value = -1e8
min_value = 1e8

for num in arr:
    if max_value < num:
        max_value = num
    if min_value > num:
        min_value = num
print(min_value, max_value)