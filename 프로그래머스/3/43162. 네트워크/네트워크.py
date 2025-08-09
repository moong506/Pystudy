def find_set(x, parents):
    if x == parents[x]:
        return x
    else:
        x = parents[x]
        
        return find_set(x, parents)

def union(x, y, parents):
    ref_x = find_set(x, parents)
    ref_y = find_set(y, parents)
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parents[x] = ref_y
    else:
        parents[y] = ref_x
    return
    
def solution(n, computers):
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                union(i, j, parents)
    answer_set = set()
    for i in range(n):
        answer_set.add(find_set(i, parents))
                
    answer = len(answer_set)
    return answer