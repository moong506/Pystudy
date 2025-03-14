def recur(num,total_heights):
    global answer
    if total_heights>=B:
        answer=min(answer,total_heights)
        return

    if num==N:
        return

    recur(num+1,total_heights+arr[num]) # 탑에 포함시키는 경우
    recur(num + 1, total_heights) # 탑에 포함시키지 않는 경우


T=int(input())
for tc in range(1,T+1):
    N,B=map(int,input().split())
    arr=list(map(int,input().split()))

    # 각 사람을 택할지 택하지 않을지를 부분집합으로 접근한다.
    answer=int(21e8)
    recur(0,0)
    print(f'#{tc} {answer-B}')