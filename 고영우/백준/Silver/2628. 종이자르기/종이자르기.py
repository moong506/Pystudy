width, height = map(int, input().split())
row = [0] * (height+1)
col = [0] * (width+1)
row[height] = 1
col[width] = 1
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:  # 가로를 자르면
        row[b] = 1
    else:
        col[b] = 1
maxR = 0
maxC = 0
last = 0
for i in range(height+1):
    if row[i] == 1:
        if maxR < i-last:
            maxR = i-last
        last = i
last = 0
for i in range(width+1):
    if col[i] == 1:
        if maxC < i-last:
            maxC = i-last
        last = i
print(maxR*maxC)