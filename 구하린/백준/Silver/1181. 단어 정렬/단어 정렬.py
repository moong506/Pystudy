N = int(input())
S = [set() for _ in range(51)] # 중복 제거를 위해 sets in list

for _ in range(N):
    string = input()
    S[len(string)].add(string) # 길이에 해당하는 인덱스의 set에 add(중복이면 안 들어감)

for i in range(1,51): # 길이 0 없으니까 1부터 시작
    if S[i]: # 해당 길이의 단어가 입력됐었으면
        sorted_set = sorted(S[i]) # 해당 세트 정렬
        for j in range(len(sorted_set)): # 하나씩 출력
            print(sorted_set[j])
    else: continue