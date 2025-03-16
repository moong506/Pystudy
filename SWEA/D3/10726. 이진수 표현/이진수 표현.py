def dec_to_bin(N, M):
    bin_list = ""

    if M == 0:
        bin_list = "0"

    else:
        while M > 0:
            remain = M % 2
            bin_list = bin_list + str(remain)
            M //= 2

    for i in range(N):
        if len(bin_list) <= i:
            return "OFF"

        if bin_list[i] == "0":
            return "OFF"

    return "ON"


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = dec_to_bin(N, M)

    print(f'#{tc} {result}')

