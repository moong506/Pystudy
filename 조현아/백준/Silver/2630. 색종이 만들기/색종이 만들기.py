# 색종이 만들기
def check_color_same(x,y,size):
    color=arr[x][y] # 첫번째 칸의 색
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j]!=color:
                return False
    return True

def recur(x,y,size):
    global white_count,blue_count
    if check_color_same(x,y,size):
        if arr[x][y]==0:
            white_count+=1
        else:
            blue_count+=1
        return

    new_size=size//2
    recur(x,y,new_size) # 왼쪽 위의 사각형
    recur(x,y+new_size,new_size)# 오른쪽 위의 사각형
    recur(x+new_size,y,new_size)# 왼쪽 아래의 사각형
    recur(x+new_size,y+new_size,new_size)# 오른쪽 아래의 사각형




N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
white_count=0
blue_count=0
recur(0,0,N)
print(white_count)
print(blue_count)