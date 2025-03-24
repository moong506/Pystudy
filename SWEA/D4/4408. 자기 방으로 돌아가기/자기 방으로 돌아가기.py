# import sys
# sys.stdin = open("input_room.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 학생 수

    corridor = [0]*200

    # 헉쓰,,, 짝 홀 나눌 필요가 없좌나
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:  # 돌아갈 방이 더 작아버리면
            start, end = end, start
        c_s, c_e = (start - 1) // 2, (end - 1) // 2
        corridor[c_s:c_e + 1] = [x + 1 for x in corridor[c_s:c_e + 1]]
    
    # 복도 값중 최대를 출력하면 됨
    print(f'#{tc} {max(corridor)}')