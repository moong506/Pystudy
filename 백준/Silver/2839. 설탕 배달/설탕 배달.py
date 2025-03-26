# 설탕배달
N=int(input())
# 일단 최대한 많은 수를 5kg의 봉지를 가져가고
# 나머지를 3kg로 하기. 만약, 나머지가 3의 배수가 아니면
# 5kg의 봉지 수를 하나씩 줄이기
remain=N%5
num_of_5=N//5

while num_of_5>=0:
    if remain%3==0:
        num_of_3=remain//3
        total=num_of_3+num_of_5
        break
    else:
        num_of_5-=1 
        remain+=5
else: # 딱 떨어지지 않는 경우 
    total=-1
print(total)

