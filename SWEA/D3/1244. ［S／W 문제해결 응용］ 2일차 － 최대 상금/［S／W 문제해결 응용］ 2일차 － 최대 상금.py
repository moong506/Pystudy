def f(i, M, N): # i 카드 위치, M 카드 수, N 남은교환횟수
    global max_v, min_cnt   # max_v를 찾았을 때의 최소 교환횟수 min_cnt
    if i == M or N == 0:      # 모든 자리를 결정했거나 교환횟수가 다 소진됐으면
        tmp = int(''.join(card))
        if max_v <= tmp:
            max_v = tmp
            if min_cnt[max_v] > N:
                min_cnt[max_v] = N

    else:
        for j in range(M):
            if i != j:      # 교환
                card[i], card[j] = card[j], card[i]
                f(i+1, M, N-1)  # 교환을 한 번 했으니 N -> N-1
                card[i], card[j] = card[j], card[i]
            else:           # i == j # 교환 횟수를 다른 자리에서 사용하도록 넘겨줌
                f(i+1, M, N)


T = int(input())

for tc in range(1, T+1):
    num, N = input().split()
    card = list(num)
    N = int(N)
    M = len(card)
    max_v = 0           # 최대 상금
    min_cnt = [10]*(10**M)       # max_v가 갱신됐을 때의 교환 횟수

    f(0, M, N)

    if min_cnt[max_v]%2:      # 남은 교환횟수가 있고, 그 횟수가 홀수면
        card[-1], card[-2] = card[-2], card[-1]
        n1 = max_v % 10       # 1의자리
        n10 = max_v % 100 // 10 # 10의 자릿수
        max_v = max_v // 100*100 + n1*10 + n10


    print(f'#{tc} {max_v}')