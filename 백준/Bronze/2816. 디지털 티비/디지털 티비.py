N = int(input())
tv_list = [input() for _ in range(N)]
a = tv_list.index('KBS1')
b = tv_list.index('KBS2')
if a < b:  # KBS2가 더 아래 있으면
    print('1' * a + '4' * a + '1' * b + '4' * (b-1))
else:
    print('1' * a + '4' * a + '1' * (b+1) + '4' * (b))