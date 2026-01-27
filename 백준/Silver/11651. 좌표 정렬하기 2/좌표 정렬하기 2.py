N = int(input())
dot_dict = {}

for i in range(N):
    x, y = map(int, input().split())
    if dot_dict.get(y):
        dot_dict[y].append(x)
    else:
        dot_dict[y] = [x]
for y in sorted(dot_dict.keys()):
    for x in sorted(dot_dict[y]):
        print(x, y)