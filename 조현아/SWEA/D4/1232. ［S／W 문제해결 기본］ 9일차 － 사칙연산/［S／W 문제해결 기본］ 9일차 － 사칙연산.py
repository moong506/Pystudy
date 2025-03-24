def in_order(T):    # 중위순회
    if not T:
        return 0

    # 노드가 연산자인 경우
    if arr[T] in ['+','-','*','/']:
        left_value=in_order(left[T])
        right_value=in_order(right[T])

        if arr[T]=='+':
            return left_value+right_value
        elif arr[T]=='-':
            return left_value-right_value
        elif arr[T]=='*':
            return left_value*right_value
        elif arr[T]=='/':
            return left_value//right_value
    else:
        return int(arr[T]) # 노드가 피연산자인 경우



T=10
for tc in range(1,T+1):
    N=int(input()) # 정점의 개수
    arr=['']*(N+1)
    left=[0]*(N+1)
    right=[0]*(N+1)

    for i in range(N): # 일단 다 입력받기
        sentence=list(input().split())
        sentence[0]=int(sentence[0])
        arr[sentence[0]]=sentence[1]

        if len(sentence)==4: # 4개이면
            sentence[2] = int(sentence[2]) # 정수로 변환하기 
            sentence[3] = int(sentence[3])

            left[sentence[0]]=sentence[2]
            right[sentence[0]]=sentence[3]

    result=in_order(1)

    print(f'#{tc} {int(result)}')