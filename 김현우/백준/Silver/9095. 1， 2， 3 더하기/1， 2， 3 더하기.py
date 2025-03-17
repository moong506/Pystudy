def f(n, sum=0):
    global count
    if sum==n:
        count += 1
        return
    elif sum>n:
        return

    for element in range(1,4):
        f(n, sum+element)

T = int(input())

for tc in range(1,T+1):
    count = 0
    f(int(input()))
    print(count)

