n = int(input()) # 1~n 정수로 수열 이룸

arr = [int(input()) for _ in range(n)] # 만들 수열
stack1 = [i for i in range(n, 0, -1)] # 값을 뽑을 스택
stack2 = [0] * n # 수열을 만들기 위한 스택
top = -1 # stack2의 top
ans = []


for a in arr:
    # stack2가 비었거나, stack2의 top이 a가 아닐 때
    if top == -1 or stack2[top] != a:
        # a까지 push
        while stack1:  # stack1이 차있는 동안
            no = stack1.pop()
            top += 1
            stack2[top] = no
            ans.append('+')
            if no == a:
                break

    # stack2의 top이 a와 같다면 pop
    if top > -1 and stack2[top] == a:
        stack2[top] = 0
        top -= 1
        ans.append('-')
    else: # top이 a와 다르다면 불가능한 경우
        ans.append('NO')
        break

if ans[-1] != 'NO':
    for i in range(len(ans)):
        print(ans[i])
else:
    print('NO')