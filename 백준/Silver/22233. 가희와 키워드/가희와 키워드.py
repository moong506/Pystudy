import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {}
count = N  # 메모장에 남은 키워드 수

for _ in range(N):
    memo[input().strip()] = 1
for _ in range(M):
    blog = input().strip().split(',')
    for keyword in blog:
        if keyword in memo:
            if memo[keyword] == 1:
                count -= 1
                memo[keyword] = 0
    print(count)