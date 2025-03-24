import sys

N,M = map(int,sys.stdin.readline().split())

not_heard = set()
not_seen = set()

for i in range(N):
    not_heard.add(sys.stdin.readline().strip())
for i in range(N):
    not_seen.add(sys.stdin.readline().strip())

both = list(not_heard & not_seen)

both.sort()

print(len(both))
for j in both:
    print(j)
