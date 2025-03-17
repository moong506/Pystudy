import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
middle = (start + end) // 2

while start < middle < end:
    get = 0
    for i in range(n):
        if tree[i] > middle:
            get += tree[i] - middle
    if get == m:
        break
    elif get < m:
        end = middle
    else:
        start = middle
    middle = (start + end) // 2
print(middle)
