T = 10
for tc in range(1, 11):
    dump = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 쌓여있는 상자 배열

    for _ in range(dump):
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if boxes[max_idx] < boxes[i]:
                max_idx = i
            if boxes[min_idx] > boxes[i]:
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1


    max_idx = 0
    min_idx = 0

    for i in range(100):
        if boxes[max_idx] < boxes[i]:
            max_idx = i
        if boxes[min_idx] > boxes[i]:
            min_idx = i

    print(f'#{tc} {boxes[max_idx] - boxes[min_idx]}')