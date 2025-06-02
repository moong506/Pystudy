W, H, N, M = map(int, input().split())
weight = W//(N+1)
height = H//(M+1)
if W % (N + 1):
    weight += 1
if H % (M + 1):
    height += 1

print(weight*height)