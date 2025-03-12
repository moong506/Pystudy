import sys
T = int(sys.stdin.readline())

for _ in range(T):
    num1, num2 = sys.stdin.readline().split()
    result = int(num1, 2) + int(num2, 2)

    print(bin(result)[2:])


'''
뭔가 구현하려고 했는데 잘 안됐습니다...
bin_dict = {'00': 0, '10': 1, '01': 1, '11':10}

T = int(sys.stdin.readline())

for _ in range(T):
    num1, num2 = map(int, sys.stdin.readline().split())
    num1, num2 = str(num1), str(num2)
    M = len(num1)
    N = len(num2)
    if M < N:
        num1, num2 = num2, num1
        M, N = N, M

    D = M-N
    result = num1[:D]
    for i in range(N):
        result += bin_dict[num1[D+1+i]+num2[i]] * 10*i
    result = num1[:D] + result
    print(result)
'''