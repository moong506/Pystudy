T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    addition = 0
    for i in range(len(arr)):
        target = arr[i]
        k = 0
        for j in range(len(target)-1, -1, -1):
            addition += int(target[j]) * (2**k)
            k += 1


    def bin_sum(n):
        result = ''
        while n>0:
            result = str(n % 2) + result
            n //= 2
        if not result:
            return 0
        return result
    print(bin_sum(addition))


