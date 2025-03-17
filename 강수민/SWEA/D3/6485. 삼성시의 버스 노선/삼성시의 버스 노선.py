T = int(input())

for tc in range(1, T + 1):
    N = int(input())  
    cnt = [0] * 5001  
    for _ in range(N):
        A, B = map(int, input().split()) 
        for i in range(A, B + 1):
            cnt[i] += 1  

    print(f'#{tc}', end=' ')
    P = int(input())
    for _ in range(P):
        C = int(input())
        print(cnt[C], end=' ')
    print()
