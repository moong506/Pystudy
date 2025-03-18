# 퀵 정렬(hoare)
def partitioning(left,right):
    pivot=A[left]
    i=left+1
    j=right

    while i<=j:
        while i<=j and A[i]<=pivot:
            i+=1
        while i<=j and A[j]>=pivot:
            j-=1
        if i<j:
            A[i],A[j]=A[j],A[i]
    A[left],A[j]=A[j],A[left]
    return j

def quick_sort(left,right):
    if left<right:
        pivot=partitioning(left,right)
        quick_sort(left,pivot-1)
        quick_sort(pivot+1,right)

A=list(map(int,input().split()))
quick_sort(0,len(A)-1)
print(A[500000])
