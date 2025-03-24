N,M,K=map(int,input().split())
count=0
while True:
    if N<2 or M<1:
        break
    else:
        if N+M-3>=K:
            N-=2
            M-=1
            count+=1
        else:
            break

print(count)