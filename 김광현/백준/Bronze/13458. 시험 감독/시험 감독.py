N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in range(len(A)):
    if A[i] >= B:
        A[i] -= B
        cnt += 1
    elif A[i] < B:
        A[i] = 0
        cnt += 1

for i in A:
    if i != 0:
        if i % C == 0:
            cnt += i // C
            i = 0
        else:
            cnt += i // C + 1
            i = 0
print(cnt)