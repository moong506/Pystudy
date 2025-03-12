def id_num(arr):
    k = 1
    while True:
        empty_list = []  # 새로운 k 값마다 리스트 초기화
        found_duplicate = False

        for i in range(len(arr)):
            remainder = arr[i] % k
            if remainder not in empty_list:
                empty_list.append(remainder)
            else:
                found_duplicate = True
                break # for문에서 나가서 while문으로 간다,.

        if not found_duplicate:
            return k  # 모든 나머지가 유일한 k 값을 찾음

        k += 1


T=int(input())
for tc in range(1,T+1):
    G=int(input())
    id=[int(input()) for _ in range(G)]
    print(id_num(id))