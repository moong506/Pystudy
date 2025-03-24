'''
그냥 처음에 sort해서 더하면 빨리 풀릴거 같지만 완전탐색으로 풀어보겠음
'''
# 재귀때문에 시간초과, 그리디로 접근
'''
def f(i,N):
    global ans, min_ans
    if i == N+1:
        for k in range(1,N+1):
            ans += p[k] * (N-k+1)
        if min_ans > ans:
            min_ans = ans
        ans = 0
        return
    else:
        for j in range(1,N+1):
            if used[j] == 0:
                used[j] = 1
                p[i] = times[j]
                f(i+1,N)
                used[j] = 0



N = int(input())
times = list(map(int,input().split()))
times = [0] + times
# 중복 x 순열
p = [0] * (N+1)
used = [0] * (N+1)
ans = 0
min_ans = 1000 * 1000 * 1001 / 2
f(1,N)
print(min_ans)
'''

N = int(input())
times = list(map(int,input().split()))
times.sort()
ans = 0
for i in range(N):
    ans += times[i] * (N-i)
print(ans)