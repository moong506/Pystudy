# start_num = 1
for i in range(1, 10001):
    for j in range(1, i):
        num = j
        while j // 10 > 0:
            num += j % 10
            j = j // 10
        num += j
        if num == i:
            # start_num = i
            break

    else: print(i)
