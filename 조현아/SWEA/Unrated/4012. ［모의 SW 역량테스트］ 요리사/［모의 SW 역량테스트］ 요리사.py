def synergy():
    a_list,b_list=[],[]
    for i in range(N):
        if visited[i]:
            a_list.append(i)
        else:
            b_list.append(i)

    a_synergy,b_synergy=0,0
    for i in range(len(a_list)):
        for j in range(i+1,len(a_list)):
            a_synergy+=(arr[a_list[i]][a_list[j]]+arr[a_list[j]][a_list[i]])

    for i in range(len(b_list)):
        for j in range(i+1,len(b_list)):
            b_synergy+=(arr[b_list[i]][b_list[j]]+arr[b_list[j]][b_list[i]])

    return a_synergy,b_synergy


def dfs(cnt,a_cnt):
    global answer
    if cnt==N//2:
        a_total,b_total=synergy()
        answer=min(answer,abs(a_total-b_total))
        return

    for food_num in range(a_cnt,N):
        if visited[food_num]:
            continue

        visited[food_num]=1
        dfs(cnt+1,food_num+1)
        visited[food_num]=0 # 원상복귀



T=int(input())
for tc in range(1,T+1):
    N=int(input()) # 식재료의 수
    arr=[list(map(int,input().split())) for _ in range(N)]

    visited=[0]*N # 재료가 사용되었음을 표시하기 위함

    answer=int(21e8)
    dfs(0,0)
    print(f'#{tc} {answer}')