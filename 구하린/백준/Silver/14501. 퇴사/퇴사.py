import sys

def generate_subsets():
    max_v = 0
    for i in range(1 << N):  # 2^N까지 반복
        subset = []
        skip = 0
        total = 0

        for j in range(N): # 
            if skip > 0: # 상담을 시작해서 상담할 수 없는 날이 남은 경우 skip > 0
                skip -= 1 # 추가 P없이 다음날(퇴사일만 가까워짐)
                continue
            if i & (1 << j): # 모든 부분집합에 대해서 시도해볼 거에요
                T, P = arr[j] # 
                if j+T<=N: # 상담을 맡기로 했는데 퇴사일 이후면 못 맡으니까 이전에 끝나는지 확인 N일째에 끝나는 것도 가능하니까 이하(<=)로
                    total += P
                    skip = T - 1 # 상담 못 맡아서 넘어가는 날 할당
                else: # 탐색하는 부분집합의 요소가 퇴사일 이후에 끝나는 거면 아예 불가능한 부분집합인거니까 바로 다음 부분집합 계산하러 갑니다
                    break # if j+T<=N
                    
            max_v = max(max_v, total) # 부분집합 검증 끝나면 이번 부분집합의 total이 최대값인지 확인 후 재할당

    return max_v # 모든 부분집합 검증 끝나면 최대값 반환

N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result = generate_subsets() # 최대값 할당
print(result)
