N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())
t_num = 0
p_num = 0
p_one = 0

# 티셔츠 구하기
for num in arr:
    t_num += num // T
    if num % T !=0:
        t_num += 1
p_num = sum(arr) // P
p_one = sum(arr) % P
print(t_num)
print(p_num, p_one)