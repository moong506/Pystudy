while True:
    R,C=map(int,input().split())
    if R==0 and C==0:
        break
    arr=[list(input()) for _ in range(R)]
    empty_list=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]!='*':
                count=0
                for di,dj in [[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    for m in range(0,2):
                        mi,mj=i+di*m,j+dj*m
                        if 0<=mi<R and 0<=mj<C:
                            if arr[mi][mj]=='*':
                                count+=1
                empty_list[i][j]=count
            else:
                empty_list[i][j]='*'
    for line in range(R):
        # empty_list[line]=''.join(map(str,empty_list[i]))
        print(''.join(map(str,empty_list[line])))