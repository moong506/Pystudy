def calc(idx, result):
    global max_result, min_result

    if idx == N:  # 모든 숫자를 다 사용했을 때
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return


    if operator[0] > 0:  # 덧셈이 있으면
        operator[0] -= 1 # 덧셈 개수 하나 줄이고
        calc(idx + 1, result + number[idx]) # 다음 숫자로 이동
        operator[0] += 1 # 연산자 사용 취소

    if operator[1] > 0:  # 뺄셈이 있으면
        operator[1] -= 1
        calc(idx + 1, result - number[idx])
        operator[1] += 1

    if operator[2] > 0:  # 곱셈이 있으면
        operator[2] -= 1
        calc(idx + 1, result * number[idx])
        operator[2] += 1

    if operator[3] > 0:  # 나눗셈이 있으면
        operator[3] -= 1
        # 음수 나눗셈 처리
        if result < 0:
            calc(idx + 1, -(-result // number[idx]))
        else:
            calc(idx + 1, result // number[idx])
        operator[3] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))  # +, -, *, /
    number = list(map(int, input().split()))

    # 최대 최소값 초기화
    max_result = -10 ** 9
    min_result = 10 ** 9

    # 첫 번째 숫자로 시작
    calc(1, number[0])

    print(f'#{tc} {max_result - min_result}')