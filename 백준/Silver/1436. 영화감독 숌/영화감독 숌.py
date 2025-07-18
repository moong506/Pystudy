import sys
input = sys.stdin.readline

N = int(input())

count = 0

for num in range(666, 3000000, 1):
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break