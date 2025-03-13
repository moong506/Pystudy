def change_num(cnt):
    global list_num, final_result, visited

    if cnt==0: # 주어진 교환 횟수를 다 사용하면,
        current_num = int(''.join(list_num))  # 문자열을 정수로 변환
        final_result = max(final_result, current_num)  # 최대값 갱신
        return

    # 반복 실행을 방지하기 위해
    current=(''.join(list_num),cnt)
    if current in visited:
        return

    visited.append(current)  # 현재 상태를 방문 목록에 추가

    N = len(list_num)  # 숫자의 자릿수
    for i in range(N):
        for j in range(i + 1, N):
            if list_num[i] == list_num[j]:  # 교환 결과가 같으므로 건너뛰기
                continue

            list_num[i], list_num[j] = list_num[j], list_num[i]  # 두 숫자 교환
            change_num(cnt - 1) # 횟수 하나 줄이기
            list_num[i], list_num[j] = list_num[j], list_num[i]  # 숫자 교환 취소




T=int(input())
for tc in range(1,T+1):
    n,c=input().split()
    list_num=list(n)
    int_count=int(c)

    visited=[]
    final_result=0

    change_num(int_count) # 함수 호출

    print(f'#{tc} {final_result}')