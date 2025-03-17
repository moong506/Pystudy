def f(i,idx): # M개 중 i번째 숫자를 arr[idx:] 중에 고르기(사전 순서 이기 때문!)
    if i == M: # M개 다 고르면
        print(*perm) # 만든 순열 출력
        return

    for j in range(idx,N): # idx -> N-1
        if used[j] == 0:
            used[j] = 1 # j번째 숫자를 썼다 표시
            perm[i] = arr[j] # 순열의 i번째 숫자는 arr[j]
            f(i+1,j+1) # arr 자체가 오름차순이라 j번 이후 부터의 수만 선택하게 인자로 전달
            used[j] = 0 # 재귀 호출 이후 다시 초기화


N,M = map(int, input().split())

arr = [i for i in range(1,N+1)] # 1부터 N까지의 숫자 리스트

perm = [0] * M
used = [0] * N

f(0,0)