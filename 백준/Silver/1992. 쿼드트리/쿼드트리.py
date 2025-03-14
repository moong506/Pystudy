def check_color_same(x,y,size):
    color=arr[x][y] # 첫번째 칸의 색
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j]!=color:
                return False
    return True

def recur(x,y,size):
    global result
    if check_color_same(x,y,size):
        if arr[x][y]=='0':
            result+='0'
        else:
            result+='1'
        return

    new_size=size//2
    result+='(' # 분할 시작 시에 괄호 열고
    recur(x,y,new_size) # 왼쪽 위의 사각형
    recur(x,y+new_size,new_size)# 오른쪽 위의 사각형
    recur(x+new_size,y,new_size)# 왼쪽 아래의 사각형
    recur(x+new_size,y+new_size,new_size)# 오른쪽 아래의 사각형
    result += ')' # 분할 끝나면 괄호 닫고



N=int(input())
arr=[list(input()) for _ in range(N)] # 문자열로..저장됨
result='' # 문자열로 저장할 최종 값.
recur(0,0,N)
print(result)