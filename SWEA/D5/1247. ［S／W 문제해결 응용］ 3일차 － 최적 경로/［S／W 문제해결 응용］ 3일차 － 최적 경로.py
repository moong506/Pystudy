def refri(curr_loc,cnt,curr_result):
    global final_result

    if not cnt:
        final_distance=curr_result+abs(curr_loc[0]-home[0])+ abs(curr_loc[1] - home[1])
        final_result = min(final_result, final_distance) # 두 값 중 최솟값 택
        return


    for i in range(len(cnt)): # 남은 고객의 수
        next_customer=cnt[i] # 다음 고객의 좌표

        dist=abs(curr_loc[0]-next_customer[0])+abs(curr_loc[1]-next_customer[1])
        remain_customer=cnt[:i]+cnt[i+1:] # 새로운 리스트로 복사
        refri(next_customer,remain_customer,curr_result+dist) # 재귀함수

T=int(input())
for tc in range(1,T+1):
    N=int(input()) # 고객의 수
    arr=list(map(int,input().split()))
    work=[arr[0],arr[1]]
    home=[arr[2],arr[3]]

    customer= []
    for i in range(4, len(arr), 2):
        if i + 1 < len(arr):
            customer.append([arr[i], arr[i + 1]]) # 2개씩 묶어서 저장.

    final_result=10**9

    refri(work,customer,0)

    print(f'#{tc} {final_result}')