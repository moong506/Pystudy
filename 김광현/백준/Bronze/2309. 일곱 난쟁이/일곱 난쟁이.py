def recur_new(idx, cnt, total, selected):  # 재귀를 통한 함수
    if cnt == 7:  # 종료 조건, 난쟁이가 7명이고
        if total == 100:  # 난쟁이의 키의 합이 100이면
            for num in sorted(selected):  # sort후 프린트
                print(num)
            exit()  # 종료
        return
    if idx >= 9 or total > 100:  # 가지치기
        return
    recur_new(idx + 1, cnt + 1, total + dwarf[idx], selected + [dwarf[idx]])  # 해당 난쟁이를 선택
    recur_new(idx + 1, cnt, total, selected)  # 해당 난쟁이를 선택 안함


dwarf = [int(input()) for _ in range(9)]
recur_new(0, 0, 0, [])