# 로또
# 재귀함수 연습
#K개의 수 중 6개를 골라 출력
def recur(cnt,start):
    if cnt==n:
        print(*path)
        return
    for i in range(start,K):
        path.append(num[i])
        recur(cnt+1,i+1)
        path.pop()

while True: # 0을 만나기 전 줄까지가 tc이다. 
    K,*num=map(int,input().split())
    if K==0:
        break
    path=[]
    n=6
    recur(0,0)
    print()

