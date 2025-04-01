# Baekjoon 3190 뱀 (2025.03.11)

# import sys
from collections import deque

# sys.stdin = open("3190_input.txt", "r")
# sys.stdout = open("3190_my_output.txt", "w")

"""
0 == 일반적인 통로
1 == 뱀
2 == 사과
"""
def play_dummy():
    # 게임 맵 만들기
    game_map = [[0] * N for _ in range(N)]
    # 사과 넣기
    for i, j in apple:
        game_map[i - 1][j - 1] = 2
    # 방향 설정
    """
    U == 상
    D == 하
    L == 좌
    R == 우
    """
    dir_dict = {
        "U": [-1, 0],
        "D": [1, 0],
        "L": [0, -1],
        "R": [0, 1]
    }
    # 맨 왼쪽 위에서, 오른쪽으로 시작
    i = j = 0
    dir = "R"
    dq = deque()
    dq.append((i, j))
    # 뱀 표시
    game_map[i][j] = 1
    # 게임 진행 시간 초기화
    play_time = 0
    while dq:
        play_time += 1
        di, dj = dir_dict[dir]
        ni, nj = i + di, j + dj
        # 벽이나 자신에게 부딪혔을 때
        if (ni < 0 or ni >= N) or (nj < 0 or nj >= N) or game_map[ni][nj] == 1:
            return play_time
        # 일반적인 상황에서 뱀의 이동
        if game_map[ni][nj] == 0:
            # 뱀 꼬리 지우기
            tail_i, tail_j = dq.popleft()
            game_map[tail_i][tail_j] = 0
        """
        뱀 이동
        사과 먹었을 때는 if game_map[ni][nj] == 0을 통과하지 않으므로,
        뱀의 꼬리를 없애지 않음
        따라서 뱀의 길이가 늘어남
        """
        dq.append((ni, nj))
        game_map[ni][nj] = 1
        i, j = ni, nj
        # 방향 전환해야 할 때
        if play_time in direction.keys():
            turn = direction[play_time]
            # 왼쪽으로 90도 회전
            if turn == "L":
                if dir == "U":
                    dir = "L"
                elif dir == "L":
                    dir = "D"
                elif dir == "D":
                    dir = "R"
                else:
                    dir = "U"
            # 오른쪽으로 90도 회전
            else:
                if dir == "U":
                    dir = "R"
                elif dir == "R":
                    dir = "D"
                elif dir == "D":
                    dir = "L"
                else:
                    dir = "U"

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
direction = {}
for l in range(L):
    X, D = input().split()
    direction[int(X)] = D
print(play_dummy())