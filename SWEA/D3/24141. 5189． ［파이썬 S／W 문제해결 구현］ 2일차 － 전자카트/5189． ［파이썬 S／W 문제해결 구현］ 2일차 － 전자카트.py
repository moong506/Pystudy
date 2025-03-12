# 순열 함수
def permutation(cnt,num_list):
    if cnt==N-1: # N=4인 경우, 1을 제외하고 234로 순열 생성.
        num_list.append([1]+path.copy()+[1]) # 새로운 변수에 저장하기 위해 얕은 복사.
        return

    for i in range(2,N+1):
        if used[i] is True:
            continue
        used[i]=True
        path.append(i)
        permutation(cnt+1,num_list)
        path.pop()
        used[i]=False

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    path = []
    used = [False] * (N+1) # 0은 무시
    per_list=[]
    permutation(0,per_list)

    min_result=10000000000 # 큰 수로 초기화

    for i in range(len(per_list)):
        result=0 # 새로운 조합을 계산할때마다 초기화
        for j in range(N):
            result+=arr[per_list[i][j]-1][per_list[i][j+1]-1] # 인덱스로 변환하기 위해 -1
        if result<min_result:
            min_result=result
    print(f'#{tc} {min_result}')