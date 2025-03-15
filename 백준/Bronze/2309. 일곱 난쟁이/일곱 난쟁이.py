# 일곱 난쟁이
# 7명을 선택하는 것이 아닌, 9명에서 2명을 빼는 방법으로 접근
def snow_white():
    global goal,height
    for i in range(9-1):
        for j in range(i+1,9):
            if height[i]+height[j]==goal:
                # 이 둘을 제외한 키 출력

                for k in range(9):
                    if k!=i and k!=j:
                        print(height[k])
                return # 한 케이스 출력한 후 종료


height=[]
for i in range(9): # 9명의 키 받아오기.
    height.append(int(input()))
height.sort() # 정렬하기
goal=sum(height)-100 # 2명 키의 합
path=[]
snow_white()

