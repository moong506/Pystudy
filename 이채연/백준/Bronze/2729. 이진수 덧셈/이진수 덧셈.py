T = int(input())
for _ in range(T):
    a, b = input().split()
    a = int(a,2)
    b = int(b,2)
    result = bin(a+b)
    print(result[2:])