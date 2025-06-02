N = int(input())
check_range = 1
count = 1
while check_range < N:
    check_range += count * 6
    count += 1

print(count)

