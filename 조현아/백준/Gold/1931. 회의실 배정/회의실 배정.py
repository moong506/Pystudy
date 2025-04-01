# 회의실 배정
N=int(input())
list_meeting=[]
for i in range(N):
    start,end=map(int,input().split())
    list_meeting.append((start,end))

# 종료 시간 기준으로 정렬, 종료 시간이 같다면 시작 시간 기준으로 정렬
list_meeting.sort(key=lambda x: (x[1], x[0]))

count=0 # 최종 개수를 저장할 변수
last=0
for i in range(N):
    if list_meeting[i][0]>=last:
        last=list_meeting[i][1]
        count+=1
    else:
        continue
print(count)
    
    
