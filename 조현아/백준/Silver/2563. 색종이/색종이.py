T=int(input()) # 종이의 수
arr=[[0]*100 for _ in range(100)] # 결과 저장용 빈 리스트 생성
result=0
for tc in range(1,T+1):
    x,y=map(int,input().split())

    for i in range(10):
        for j in range(10):
            arr[x+i][y+j]=1

for k in range(100):
    for m in range(100):
        if arr[k][m]==1:
            result+=1

print(f'{result}')