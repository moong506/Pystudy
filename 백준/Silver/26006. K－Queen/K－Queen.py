N, K = map(int, input().split())  # N:체스판의 크기, K:흑색 퀸의 수
WR, WC = map(int, input().split())  # 백색 킹의 위치
WR -= 1
WC -= 1
black = [list(map(int, input().split())) for _ in range(K)]  # K개의 흑색 퀸의 위치
# 인덱스와 일치하도록 조정
for i in range(K):
    black[i][0] -= 1
    black[i][1] -= 1

# 특정 위치가 퀸에게 공격받는지 확인하는 함수
def is_attacked(i, j):
    for qi, qj in black:
        # 같은 행
        if i == qi:
            return True
        # 같은 열
        if j == qj:
            return True
        # 대각선
        if abs(i - qi) == abs(j - qj):
            return True
    return False

# 킹이 공격받고 있는지 확인
king_is_attacked = is_attacked(WR, WC)

# 킹이 움직일 수 있는 위치가 있는지 확인
can_move = False
for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
    nr, nc = WR + dr, WC + dc
    if 0 <= nr < N and 0 <= nc < N and not is_attacked(nr, nc):
        can_move = True
        break

# 결과 판정
result = 'NONE'
if king_is_attacked:
    if can_move:
        result = 'CHECK'  # 공격받고 있지만 움직일 수 있음
    else:
        result = 'CHECKMATE'  # 공격받고 있고 움직일 수 없음
elif not can_move:
    result = 'STALEMATE'  # 공격받지 않지만 움직일 수 없음

print(result)