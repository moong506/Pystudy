arr = input()
N = len(arr)
top = 0
cnt = 0
i = 0
while i < N:
    if arr[i] =='(':
        if arr[i+1] ==')':
            cnt += top
            i += 1  # ')' 패스해주기
        else:  # arr[i+1] == '('
            top += 1
    else:  # arr[i] == ')'
        cnt += 1
        top -= 1
    i += 1

print(cnt)