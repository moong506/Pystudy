N = int(input())
arr = list(map(int, input().split()))

line = [0]*N        # 배치해줄 빈 리스트
for i in range(N):  # arr에서 꺼내서 배치해줄 거임
    higher = arr[i]   # 왼쪽에 있어야 할 큰 사람
    for j in range(N):  # 왼쪽에서 부터 빈 자리 찾기
        if line[j] == 0:    # 빈 자리라면
            if higher == 0:    # 왼쪽에 있어야 할 사람이 이제 없다면
                line[j] = i+1   # 바로 그 자리 입니다! 푸핫
                break
            higher -= 1    # 아직 왼쪽 자리 남았으니까 -

print(*line)