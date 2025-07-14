# 괄호
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    PS = list(sys.stdin.readline().strip())
    top = 0
    flag = True
    for word in PS:
        if word == '(':
            top += 1
        else:
            top -= 1
            if top == -1:
                flag = False
                break
    else:
        if top > 0:
            flag = False
# 최종 판정
    if flag is False:
        print('NO')
    else:
        print('YES')
