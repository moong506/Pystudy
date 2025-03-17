T=int(input())
for tc in range(1,T+1):
    num1,num2=input().split() # 리스트로 입력받기
    l_num1 = list(map(int, num1))
    l_num2 = list(map(int, num2))

    if len(l_num1)>=len(l_num2):
        max_num=l_num1
        min_num=l_num2
    else:
        max_num=l_num2
        min_num=l_num1

    # 짧은 숫자 앞에 0을 2개, 긴 숫자 앞엔 0 1개 추가로 붙이기.
    # 넘어가는 숫자를  처리하기 위함
    min_num = [0] * (len(max_num) - len(min_num)) + min_num

    max_num = [0] + max_num
    min_num = [0] + min_num

    result='' # 결과 저장
    carry=0 # 넘어가는 숫자를 처리하기 위함

    for i in range(len(max_num)-1,-1,-1): #뒤에서부터 더하기
        num=max_num[i]+min_num[i]+carry

        if num>=2:
            carry=1
            result=str(num-2)+result
        else:
            carry=0
            result=str(num)+result

    # 앞의 불필요한 0 제거
    if '1' in result:
        final_result = result.lstrip('0')
    else:
        final_result = '0'  # 결과가 모두 0인 경우

    print(final_result)