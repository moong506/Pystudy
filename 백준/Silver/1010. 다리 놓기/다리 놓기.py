T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # 분모는 N!
    # 분자는 M*M-1*M-2 ... N개까지만
    a = b = 1  # 분모 b, 분자 a

    for i in range(N):
        a *= M-i
        b *= i+1
    print(a//b)
