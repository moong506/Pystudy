N = int(input())
arr = list(map(int, input().split()))
stu_num = int(input())
new_stu_num = [2]*(N+1)
for i in range(1,N+1):
    new_stu_num[i] = arr[i-1]
for _ in range(stu_num):
    gender, number = map(int, input().split())
    if gender == 1:
        a = number
        while number <= N:
            if new_stu_num[number] == 0:
                new_stu_num[number] = 1
            elif new_stu_num[number] == 1:
                new_stu_num[number] = 0
            number += a
    elif gender == 2:
        i = 0
        while 1<=number - i and number +i <= N:
            if new_stu_num[number-i] == new_stu_num[number+i]:
                i += 1
                if number-i< 1 or number+i > N:
                    for j in range(number-(i-1),number+i):
                        if new_stu_num[j] == 0:
                            new_stu_num[j] = 1
                        elif new_stu_num[j] ==1:
                            new_stu_num[j] = 0
                    break
                continue
            elif new_stu_num[number-i] != new_stu_num[number+i]:
                for j in range(number-(i-1),number+i):
                    if new_stu_num[j] == 0:
                        new_stu_num[j] = 1
                    elif new_stu_num[j] == 1:
                        new_stu_num[j] = 0
                break
for i in range(1,N+1):
    print(new_stu_num[i], end = ' ')
    if i % 20 == 0 and i!= 1:
        print()
