def recur(cnt, total):
    if cnt == 7:  # 7명을 선택했을 때
        if total == 100:  # 키의 합이 100이면 출력
            path.sort()  # 선택된 난쟁이들 정렬
            for h in path:
                print(h)
            exit()  # 첫 번째 정답을 찾으면 프로그램 종료
        return

    for i in range(9):
        if not used[i]:  # 아직 선택되지 않은 난쟁이
            used[i] = 1  # 선택
            path.append(num[i])  # 경로 저장
            recur(cnt + 1, total + num[i])  # 다음 단계 재귀 호출
            path.pop()  # 백트래킹 (이전 선택 취소)
            used[i] = 0  # 백트래킹 (선택 해제)


num = [int(input()) for _ in range(9)]  # 9명의 키 입력
path = []  # 선택된 난쟁이 저장
used = [0] * 9  # 선택된 난쟁이 여부 체크
recur(0, 0)
