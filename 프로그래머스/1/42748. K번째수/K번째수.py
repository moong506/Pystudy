def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        part_arr = array[i-1:j]
        part_arr.sort()
        answer.append(part_arr[k-1])
    
    return answer