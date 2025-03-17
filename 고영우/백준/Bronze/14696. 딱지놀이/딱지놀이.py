N = int(input())
for _ in range(N):
    arr_A = []
    arr_B = []
    cnt_4_A = 0
    cnt_3_A = 0
    cnt_2_A = 0
    cnt_1_A = 0
    cnt_4_B = 0
    cnt_3_B = 0
    cnt_2_B = 0
    cnt_1_B = 0
    number_A, *ttakjji_A = map(int, input().split())
    arr_A.append(ttakjji_A)
    number_B, *ttakjji_B = map(int, input().split())
    arr_B.append(ttakjji_B)
    for i in range(len(ttakjji_A)):
        if ttakjji_A[i] == 4:
            cnt_4_A += 1
        elif ttakjji_A[i] == 3:
            cnt_3_A += 1
        elif ttakjji_A[i] == 2:
            cnt_2_A += 1
        else:
            cnt_1_A += 1
    for i in range(len(ttakjji_B)):
        if ttakjji_B[i] == 4:
            cnt_4_B += 1
        elif ttakjji_B[i] == 3:
            cnt_3_B += 1
        elif ttakjji_B[i] == 2:
            cnt_2_B += 1
        else:
            cnt_1_B += 1
    if cnt_4_A > cnt_4_B:
        print('A')
    elif cnt_4_A < cnt_4_B:
        print('B')
    elif cnt_4_A == cnt_4_B:
        if cnt_3_A > cnt_3_B:
            print('A')
        elif cnt_3_A < cnt_3_B:
            print('B')
        elif cnt_3_A == cnt_3_B:
            if cnt_2_A > cnt_2_B:
                print('A')
            elif cnt_2_A < cnt_2_B:
                print('B')
            elif cnt_2_A == cnt_2_B:
                if cnt_1_A > cnt_1_B:
                    print('A')
                elif cnt_1_A < cnt_1_B:
                    print('B')
                elif cnt_1_A == cnt_1_B:
                    print('D')

