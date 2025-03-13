# 회의실 배정
N = int(input())    # 회의 수
# 시작시간과 종료시간
time = []
for _ in range(N):
    s, e = map(int, input().split())
    time.append([s, e])

time.sort(key=lambda x:(x[1], x[0]))
end_time = 0  # 처음 종료 시간 0
cnt = 0

for s, e in time:
    if s >= end_time:
        cnt+=1
        end_time = e
print(cnt)