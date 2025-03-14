def recur(amount,month):
    global final_amount
    if final_amount < amount:
        return

    if month > 12:
        final_amount = min(final_amount, amount)
        return


    # 1일 이용권을 구매하는 경우
    recur(amount + (day_1 * arr[month]), month + 1)

    # 1달 이용권을 구매하는 경우
    recur(amount + month_1, month + 1)

    # 3달 이용권을 구매하는 경우
    recur(amount + month_3, month + 3)

    # 1년 이용권을 구매하는 경우
    recur(amount + year_1, month + 12)



T=int(input())
for tc in range(1,T+1):
    day_1,month_1,month_3,year_1=map(int,input().split())
    arr=[0]+list(map(int,input().split()))

    final_amount=int(21e9)

    recur(0, 1)
    
    print(f'#{tc} {final_amount}')