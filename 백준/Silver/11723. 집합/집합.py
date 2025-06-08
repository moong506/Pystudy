import sys
input = sys.stdin.readline
N = int(input())
S = [0]*21
for _ in range(N):
    command = input().split()
    op = command[0]
    if op == 'all':
        for i in range(1,21):
            S[i] = 1
    elif op == 'empty':
        for i in range(1, 21):
            S[i] = 0
    else:
        num = int(command[1])
        if op == 'add':
            S[num] = 1
        elif op == 'remove':
            S[num] = 0
        elif op == 'check':
            print(S[num])
        else:  # op == 'toggle':
            S[num] = 1 - S[num]
