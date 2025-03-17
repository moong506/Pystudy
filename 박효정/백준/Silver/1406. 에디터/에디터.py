s1 = list(input()) # 왼쪽 스택
s2 = [] # 오른쪽 스택
M = int(input())    # 입력할 명령어 개수
arr = [list(input().split()) for _ in range(M)] # 명령어

# 커서를 기준으로 왼쪽, 오른쪽으로 스택을 나눠 관리한다는 발상

for a in arr: # 명령읽기
    if a[0] == 'L' and s1: # s1이 차있을때(커서가 맨 왼쪽이 아닐 때) / 커서 왼쪽으로 한 칸 옮김
        s2.append(s1.pop())

    elif a[0] == 'D' and s2: # s2가 차있을때(커서가 맨 오른쪽이 아닐 때) / 커서 오른쪽으로 한 칸 옮김
        s1.append(s2.pop())

    elif a[0] == 'B' and s1: # s1이 차있을때(커서가 맨 왼쪽이 아닐 때) / 커서 왼쪽 문자 삭제
        s1.pop()

    elif a[0] == 'P': # P$ / 커서 왼쪽에 문자$ 추가
        s1.append(a[1])


print("".join(s1 + s2[::-1]))  # 결과 출력 / stck2는 뒤집어서 읽어야함 