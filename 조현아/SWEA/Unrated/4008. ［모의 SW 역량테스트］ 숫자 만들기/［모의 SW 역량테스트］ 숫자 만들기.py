def dfs(idx, result):
    global max_result, min_result

    # 종료 조건
    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if operators[0] > 0:  # +
        operators[0] -= 1
        dfs(idx + 1, result + numbers[idx])
        operators[0] += 1
    if operators[1] > 0:  # -
        operators[1] -= 1
        dfs(idx + 1, result - numbers[idx])
        operators[1] += 1
    if operators[2] > 0:  # *
        operators[2] -= 1
        dfs(idx + 1, result * numbers[idx])
        operators[2] += 1
    if operators[3] > 0:  # /
        operators[3] -= 1
        if result < 0:
            dfs(idx + 1, -(-result // numbers[idx]))
        else:
            dfs(idx + 1, result // numbers[idx])
        operators[3] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 숫자의 개수
    operators = list(map(int, input().split()))  # +, -, *, / 연산자 개수
    numbers = list(map(int, input().split()))  # 숫자들

    max_result = -float('inf')
    min_result = float('inf')

    dfs(1, numbers[0])

    # 최대값과 최소값의 차이
    result = max_result - min_result

    print(f'#{tc} {result}')