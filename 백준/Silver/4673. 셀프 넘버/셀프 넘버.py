exist_num=[] # 셀프넘버를 저장할 변수

for i in range(1,10001):
    next_num=i
    step=i
    while step>0:
        next_num+=step%10
        step//=10
    if next_num<10001:
        exist_num.append(next_num) #  존재 체크


for j in range(1,10001):
    if j not in exist_num:
        print(j)