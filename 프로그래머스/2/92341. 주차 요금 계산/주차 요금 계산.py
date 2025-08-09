def solution(fees, records):
    # 1. 같은 차 번호끼리 모으기
    car_dict = {}
    for record in records:
        time = record[:5]
        car = record[6:10]
        if car in car_dict.keys():
            car_dict[car].append(time)
        else:
            car_dict[car] = [time]

    # 2. 번호끼리 계산하기
    car_num = sorted(car_dict.keys())
    answer = [0]*len(car_dict.keys())
    idx = 0
    for num in car_num:
        count = 0
        if len(car_dict[num]) % 2 == 1:
            car_dict[num].append('23:59')
        for i in range(0, len(car_dict[num]), 2):
            hour = int(car_dict[num][i+1][:2]) - int(car_dict[num][i][:2])
            minute = int(car_dict[num][i+1][3:]) - int(car_dict[num][i][3:])
            count += hour*60 + minute
        answer[idx] = fees[1] + max(count - fees[0], 0) // fees[2] * fees[3]
        if count > fees[0] and (count-fees[0]) % fees[2] != 0:
            answer[idx] += fees[3]
            
        idx += 1

    return answer