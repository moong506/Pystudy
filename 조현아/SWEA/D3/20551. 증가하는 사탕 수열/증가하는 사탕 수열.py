T=int(input())
for tc in range(1,T+1):
    a,b,c=map(int,input().split())

    num=0
    while True:
        if b>=c: # 뒤에서 부터 탐색을 해서 일단 뒤에 두 상자의 개수 차이를 완성한다.
            num+=1
            b-=1
        elif a>=b: # 뒤에 2개가 완성되면 앞에 2개를 완성시킨다.
            num+=1
            a-=1
        else:
            if num>=(a+b+c): # 만약 사탕을 다 먹어버린 경우 1을 넘겨야하는 조건을 위반하므로 -1 출력
                result=-1
                break
            elif a==0: # 가장 작은 수의 사탕이 0인 경우
                result = -1
                break
            else:
                result=num # 나머지의 경우 먹은 총 사탕의 수 출력
                break

    print(f'#{tc} {result}')