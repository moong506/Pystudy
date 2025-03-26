T = int(input())

for _ in range(T):
    N = int(input())

    a,b = 1,0 # N이 0 일 때 0과 1의 호출 횟수 (초기화 값)

    for _ in range(N):
        a,b = b, a+b # N의 (0의 호출 횟수, 1의 호출 횟수) == N-1의 (1의 호출 횟수, 0과 1의 호출 횟수의 합) 

    print(a, b) # 0과 1의 호출 횟수 누적값