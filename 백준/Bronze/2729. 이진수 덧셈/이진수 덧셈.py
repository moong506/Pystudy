def to_decimal(bin):  # 2진수를 10진수로 변환
    dec_num = 0
    rev_bin = ""

    # 2진수를 10진수로 변환하려면 뒤에서부터 2의 제곱을 해줘야되기 때문에 역순으로 저장
    for i in range(len(bin)-1, -1, -1):
        rev_bin += bin[i]

    for i in range(len(rev_bin)):
        if int(rev_bin[i]) == 1:  # 1이면 i의 값에 맞게 제곱해줘야함
            dec_num += 2 ** i

    return dec_num


def to_binary(dec):  # 10진수를 2진수로 변환
    if dec == 0:
        return '0'

    binary = ""
    while dec > 0:  # 0이 될 때 까지
        remain = dec % 2  # 나머지 값 구하기
        binary = str(remain) + binary  # 문자열에 추가
        dec //= 2  # 몫 구하기

    return binary


T = int(input())

for tc in range(1, T+1):
    first, second = input().split()

    # 10진수 변환
    x = to_decimal(first)
    y = to_decimal(second)
    dec_sum = x + y

    # 2진수 변환
    print(to_binary(dec_sum))
