C = int(input())
for _ in range(C):
    N, *scores = list(map(int, input().split()))
    # print(*scores)

    # 평균 구하기
    average = sum(scores) / N

    # 평균을 넘는 학생의 비율 구하기
    stu_lst = []
    for i in scores:
        if i > average:
            stu_lst.append(i)

    ans = round((len(stu_lst)/N)*100, 3)

    print(f'{ans}%')