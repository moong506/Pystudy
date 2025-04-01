T = int(input())
for t in range(T):
    s = input()
    a = 1
    if s != s[::-1]:
        a = 0
 
    print(f"#{t + 1} {a}")