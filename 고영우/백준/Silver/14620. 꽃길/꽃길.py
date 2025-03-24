def get_cost(i,j):
    s= 0
    position = []
    for di, dj in [[0,0], [0,1], [1,0], [0,-1], [-1,0]]:
        ni, nj = i + di, j + dj
        if ni<0 or ni>=N or nj <0 or nj>=N:
            continue
        s += arr[ni][nj]
        position.append((ni,nj))
    return s, position

def combination_lst(lst):
    result = []
    def backtrack(i,current):
        if len(current) == 3:
            result.append(current[:])
            return
        else:
            for j in range(i,len(lst)):
                current.append(lst[j])
                backtrack(j+1, current)
                current.pop()
    backtrack(0,[])
    return result

def min_cost():
    positions = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            s, position = get_cost(i,j)
            positions.append((s, position))
    min_cost = float('inf')
    # 이 부분 헷갈림 주의
    for combination in combination_lst(positions):
        p1, p2, p3 = combination[0][1], combination[1][1], combination[2][1]
        if len(set(p1+p2+p3)) == 15:
            min_cost = min(min_cost, combination[0][0] + combination[1][0] + combination[2][0])
    return min_cost



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(min_cost())