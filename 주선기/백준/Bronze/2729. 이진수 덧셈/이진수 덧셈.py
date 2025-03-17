# Baekjoon 2729 이진수 덧셈 (2025.03.09)

# import sys

# sys.stdin = open("2729_input.txt", "r")
# sys.stdout = open("2729_my_output.txt", "w")

# 재귀 함수를 이용한 10진수를 2진수로 변환하는 법
def transform_dec_to_bin(n):
    # 종료 조건
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return transform_dec_to_bin(n // 2) + str(n % 2)

# 내장 함수 이용하지 않은 버전
T = int(input())
for _ in range(T):
    A, B = input().split()
    # A 2진수에서 10진수로 변경
    dec_A = 0
    for i in range(len(A)):
        dec_A += (2 ** i) * int(A[len(A) - 1 - i])
    # B 2진수에서 10진수로 변경
    dec_B = 0
    for i in range(len(B)):
        dec_B += (2 ** i) * int(B[len(B) - 1 - i])
    # A + B 후, 10진수에서 2진수로 변경 후, 출력
    print(transform_dec_to_bin(dec_A + dec_B))

# 내장 함수 이용 버전
# T = int(input())
# for _ in range(T):
#     A, B = input().split()
#     # 2진수를 10진수로 변환
#     dec_A = int(A, 2)
#     dec_B = int(B, 2)
#     # 덧셈 수행 후 2진수 변환
#     result = bin(dec_A + dec_B)[2:]
#     print(result)
