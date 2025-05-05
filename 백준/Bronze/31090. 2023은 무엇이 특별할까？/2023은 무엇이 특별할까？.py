T = int(input())
for tc in range(1,T+1):
    N = int(input())
    if (N+1) % (N % 100) == 0:
        print('Good')
    else:
        print('Bye')