T=int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    if tc!=T:
        a=input()
    # print(arr)

    # 행 검색
    result="CORRECT"
    for i in range(9):
        empty_list_1=[]
        for j in range(9):
            if arr[i][j] in empty_list_1:
                result="INCORRECT"
            else:
                empty_list_1.append(arr[i][j])

    # 열 검색
    for j in range(9):
        empty_list_2=[]
        for i in range(9):
            if arr[i][j] in empty_list_2:
                result="INCORRECT"
            else:
                empty_list_2.append(arr[i][j])

    # 3*3 박스 검색
    for di,dj in [[0,0],[0,3],[0,6],
                [3,0],[3,3],[3,6],
                [6,0],[6,3],[6,6]]:
        empty_list_3=[]
        for i in range(3):
            for j in range(3):
                mi=di+i
                mj=dj+j
                if arr[mi][mj] in empty_list_3:
                    result="INCORRECT"
                else:
                    empty_list_3.append((arr[mi][mj]))
    print(f'Case {tc}: {result}')