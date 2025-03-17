def dec_to_bin(N, M):
    bin_list = ""  # 이진수를 저장할 문자열 초기화

    if M == 0:  # M이 0인 경우 처리
        bin_list = "0"

    else:  # M이 0이 아닌 경우
        while M > 0:  # M이 0보다 클 때까지 반복
            remain = M % 2
            bin_list = bin_list + str(remain)  # 나머지를 문자열에 추가
            M //= 2

    # 마지막 N비트가 모두 1인지 확인
    for i in range(N):
        if len(bin_list) <= i:  # 이진수 표현의 길이가 N보다 작으면 OFF 반환
            return "OFF"

        if bin_list[i] == "0":  # i번째 비트가 0이면 OFF 반환
            return "OFF"

    return "ON"  # 모든 조건 통과하면 ON 반환


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = dec_to_bin(N, M)

    print(f'#{tc} {result}')

